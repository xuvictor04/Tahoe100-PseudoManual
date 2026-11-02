# Per-line p53 function in the 50 lines, and whether it changes the MG53 results

Scope note. This answers two things: (1) has each TP53 mutant been assessed for whether it raises or lowers
p53 output, and (2) does using that finer picture, instead of a yes/no genotype label, change what MG53's
level does to p53 (downstream of MG53). Whether p53 regulates MG53 is out of scope: the section that asked
whether TRIM72's induction depends on p53 function has been removed, along with the cardiac-glycoside lead,
which rested on the same question.

Produced by a 12-agent workflow in which every number was independently recomputed by an adversarial
verifier. Per-line values are in `tables/per_line_p53_state.csv` (key columns) and
`tables/per_line_p53_state_FULL.csv` (all 216 columns); mutation annotation in
`tables/tp53_mutation_annotation.csv` and `tables/tp53db_variant_function.csv`.

## 1. Short answer

- **Each line has been considered, but mostly only as a yes/no genotype.** The list-free primary MG53 test uses the binary label: WT-minus-altered program-P slope **−0.00183**, two-way p 0.285, TP53-label-permutation p 0.304 [`genome_wide/tables/c_program_models.csv` row 0]. None of its covariate sets (gw, gw_all, gw_pc, curated_cycle, none, gw_rt) holds responsiveness, mutation class, or a "direction of p53 change" term [REPO `mg53_p53/genome_wide/genome_wide.py` ~l.128]. For the literal question "were all mutants considered": the primary gw model is actually fit on **17 WT + 30 altered** lines — NCI-H661 (no TRIM72), NCI-H2122 and NCI-H596 (no exposure) drop out, so three altered lines are not even in it (recomputed; [row 0 n_rows 53,084]). The covset-none version uses 17/32 [row 4, −0.00230, 53,331 rows].
- **What *was* considered beyond the label.** Graded panel responsiveness enters as a secondary grouping in named steps only: `p53_dependence` (pooled sets), `single_cell_all`, and as a covariate (not a slope-moderator) in `two_way` [`two_way/tables/key_results.csv` row 42]. **Mutation class** (missense-only vs truncating/splice/deletion) appears only in `p53_dependence`, and only against WT, never missense-vs-truncating directly. **Hotspot status, CDKN2A, ATM** appear only as rival groupings or ambient controls, never as a modifier of p53 in WT lines.
- **What was never asked.** No analysis placed each mutant on a p53 axis against a null and asked "above (retained / up) or below (dominant-negative / down)?" The repository's own genotype-blind panel gives the cleanest single-table answer to the direction question: of the "discordant" calls, there are **zero** "altered-but-responsive" lines — not one mutant crosses the responsive cut — and exactly one "WT-but-unresponsive" line, Hs 766T [`p53_dependence/tables/lines_tp53_status.csv`, recomputed]. So on this readout no mutant up-regulates p53, and none is credibly below the null either.
- **Down-regulation below a null (dominant-negative) does not apply in most lines.** 30 of 33 altered lines have strong sequence evidence of no remaining WT TP53 allele (CCLE VAF ≈1.0, deleted, or compound), so there is no WT allele for a mutant to poison; AN3 CA and NCI-H2122 may keep a functional allele, and HCT15/Panc 03.27 are unphased (literature overlay; the earlier "32 lines, all null-equivalent" was an overstatement).
- **Downstream (MG53 → p53-program): accounting for direction changes nothing robust.** Deconfounded graded moderators per SD of function: responsiveness **−0.0011** (p_perm 0.24), inducibility **−0.0014** (0.16), basal **−0.0014** (0.19); within genotype ≈0. Functional-group contrasts null (responsive−unresponsive −0.0013, p 0.59). Across ~24 tests the smallest multiplicity-corrected q is **0.54** (recomputed). The one lead that survives dropping influential lines is a *post-hoc, borderline* one: basal TP53 mRNA as a within-genotype moderator, **+0.0019/SD, p_perm 0.002**, concentrated in altered lines (missense/high-mRNA mutants steeper) — not an established result.
- **The MG53→p53 association sits in the wrong place for a p53-mediated effect.** In the primary model the slope is in the altered lines (b_alt +0.0026, drug-level p 3e-6; b_WT +0.0009, ns) [row 0], and in the repository's own split it is largest in the *lowest*-activity mutants (+0.0043) and absent in WT and higher-activity mutants [REPO `mg53_p53/findings/tables/tableC_mutants_by_activity.csv`]. An effect routed through p53 cannot be strongest where p53 is deadest — this points to a stress-amplitude confound, not to p53 direction.

---

## 2. Per-line reading — all 50 lines, sorted by data-defined inducibility

Columns: genotype label (data) · TP53 variant and zygosity (literature overlay) · literature class and expected direction (overlay) · `ind_P_mean` / `ind_P_slope` (data-defined) · panel responsiveness and call (list-based) · basal p53 (within-plate z, list-based) · TP53 mRNA (data-defined, one gene) · combined reading (data) · flag. Sources: [`line_state/per_line_p53_state.csv`], [`mutations/line_expected_p53_output.csv`], [`p53_dependence/tables/lines_tp53_status.csv`], [`downstream_p53/tables/b_baseline_per_line.csv`]; all per-line values recomputed by the readers. Combined reading is relative to the null reference (b_p53 null-core median 0.039). No line is credibly *below* null.

| Line | Geno | TP53 variant (zygosity) | Lit. class → expected dir | ind_P_mean / slope | Panel resp (call) | basal z | TP53 mRNA | Combined reading | Flag |
|---|---|---|---|---|---|---|---|---|---|
| NCI-H460 | WT | — | functional → up | 0.184 / 3.09 | 1.25 (resp) | +0.47 | 4.40 | functional, above | |
| RKO | WT | — | functional → up | 0.168 / 2.86 | 1.37 (resp) | +0.43 | 4.22 | functional, above | |
| A549 | WT | — (CDKN2A del) | functional → up | 0.158 / 2.58 | 0.98 (resp) | +1.25 | 8.18 | functional, above | |
| SNU-1 | WT | — (MDM4 high, ATM fs) | attenuated → down | 0.154 / 2.55 | 1.06 (resp) | +0.33 | 3.72 | functional, above | lit "attenuated" vs data functional |
| A498 | WT | — (VHL loss, CDKN2A del) | attenuated → down | 0.152 / 3.01 | 1.10 (resp) | +1.00 | 6.97 | functional, above | lit "attenuated" vs data functional |
| H4 | WT | — (CDKN2A/PTEN del) | functional → up | 0.150 / 2.50 | 0.71 (unc) | +0.57 | 4.90 | functional, above | |
| SW48 | WT | — | functional → up | 0.150 / 2.81 | 1.06 (resp) | +0.78 | 5.92 | functional, above | |
| A-172 | WT | — (PPM1D gain, CDKN2A del) | functional → up | 0.147 / 2.93 | 0.72 (unc) | +0.96 | 6.77 | functional, above | |
| C32 | WT | — (MDM4 amp) | attenuated → down | 0.147 / 2.17 | 1.04 (resp) | +0.71 | 5.58 | functional, above | lit "attenuated" vs data functional |
| LS 180 | WT | — | functional → up | 0.145 / 2.89 | 0.95 (resp) | +1.04 | 7.17 | functional, above | |
| hTERT-HPNE | WT | — (normal cell) | functional → up | 0.135 / 2.43 | 0.94 (resp) | +0.75 | 5.75 | functional, above | |
| LoVo | WT | — | functional → up | 0.117 / 2.15 | 1.03 (resp) | +0.94 | 6.67 | functional, above | |
| LOX-IMVI | WT | — (CDKN2A del) | functional → up | 0.116 / 2.12 | 0.72 (unc) | +0.80 | 6.01 | functional, above | |
| A-427 | WT | — (CDKN2A del) | functional → up | 0.096 / 1.83 | 0.66 (unc) | +0.62 | 5.12 | functional, above | |
| CHP-212 | WT | — (PPM1D/MDM4 gain) | functional → up | 0.083 / 1.96 | 0.56 (unc) | +0.75 | 5.78 | functional, above | |
| HepG2/C3A | WT | — | functional (ext. conflict) → up | 0.076 / 1.51 | 0.90 (resp) | +0.59 | 4.96 | functional, above | nutlin-resistant externally |
| J82 | alt | E271K (homoz, 6 reads); K320N (VAF 0.30) | missense partial (yeast) → up | 0.027 / 0.86 | 0.60 (unc) | −0.34 | 0.46 | residual (partial), slightly above | human-cell assays call E271K LOF; conf. weak |
| NCI-H23 | alt | M246I (homoz) | missense LOF/conflicting → null | 0.025 / 1.07 | 0.31 (unresp) | −0.11 | 1.58 | marginal residual | lit null vs data slight residual |
| HEC-1-A | alt | R248Q (homoz, hotspot) | GOF; canonical null → non-canon | 0.022 / 0.98 | 0.29 (unresp) | −0.53 | −0.44 | marginal residual | GOF invisible to canonical P |
| HOP62 | alt | splice c.673-2A>G (homoz) | splice-null → null | 0.020 / 1.00 | 0.34 (unresp) | −0.59 | −1.71 | flags residual, but is a null line | calibration: ~1 of 10 null lines does this |
| BT-474 | alt | E285K (homoz, temp-sensitive) | missense ts → near-null @37 °C | 0.019 / 1.26 | 0.50 (unc) | −0.34 | 0.50 | residual (partial) | robust residual; protein ts invisible |
| MIA PaCa-2 | alt | R248W (homoz, hotspot) | GOF; canonical null → non-canon | 0.019 / 1.12 | 0.47 (unc) | −0.54 | −0.51 | marginal residual | GOF invisible |
| SW480 | alt | R273H;P309S (cis, LOH, hotspot) | GOF → non-canon | 0.017 / 0.98 | 0.22 (unresp) | −0.30 | 0.65 | null-like | GOF invisible |
| HS-578T | alt | V157F (homoz, LOH) | missense LOF → null-eq | 0.017 / 0.91 | 0.33 (unresp) | −0.47 | −0.14 | marginal residual | |
| NCI-H2030 | alt | G262V (homoz) | missense LOF (borderline) → null-eq | 0.016 / 0.88 | 0.20 (unresp) | −0.20 | 1.16 | null-like | |
| NCI-H2347 | alt | c.375G>A T125T splice (homoz) | splice-null → null | 0.016 / 0.62 | 0.41 (unresp) | +0.39 | −1.73 | null-like on P, high basal (z 4.0) | mixed |
| PANC-1 | alt | R273H (homoz, hotspot) | GOF → non-canon | 0.010 / 0.91 | 0.26 (unresp) | −0.38 | 0.27 | null-like | GOF invisible |
| SW 900 | alt | Q167* (homoz) | nonsense-null → null | 0.010 / 0.90 | 0.31 (unresp) | −0.46 | −0.24 | null-like | |
| AN3 CA | alt | G389W; R213Q; S90fs (subclonal, VAF ≤0.5) | mixed (R213Q DNE, G389W funct.) → uncertain/up | 0.010 / 0.93 | 0.47 (unc) | +0.12 | 2.73 | residual — strongest altered (b_p53 0.32), basal z 2.7 | robust residual; classed "truncating" in repo |
| C-33 A | alt | R273C (homoz, hotspot) | GOF → non-canon | 0.009 / 0.74 | 0.24 (unresp) | −0.40 | 0.16 | null-like | GOF invisible |
| Hs 766T | **WT** | — (WT sequence) | WT but pathway likely inactive → down | 0.008 / 0.65 | 0.16 (unresp) | −0.91 | 0.47 | null-like | **FLAG: WT genotype, behaves like a mutant** (discordant) |
| SK-MEL-2 | alt | G245S (homoz/LOH, hotspot) | GOF/DNE → non-canon | 0.008 / 0.85 | 0.12 (unresp) | −0.32 | 0.58 | null-like | GOF invisible |
| SW1417 | alt | C238fs (hemizygous, VAF 1.0) | frameshift-null → null | 0.008 / 0.69 | 0.19 (unresp) | −0.12 | 1.85 | null-like | |
| Panc 03.27 | alt | 375+5G>T splice (homoz) | splice-null → null | 0.007 / 0.74 | 0.26 (unresp) | −0.31 | 0.72 | null-like | |
| HT-29 | alt | R273H (homoz, LOH, hotspot) | GOF → non-canon | 0.004 / 0.70 | 0.05 (unresp) | −0.02 | 2.03 | null-like | GOF invisible |
| RPMI-7951 | alt | S166* (homoz) | nonsense-null → null | 0.004 / 0.62 | 0.28 (unresp) | −0.41 | 0.24 | null-like | |
| KATO III | alt | TP53 homozygous deletion | deletion-null (**null anchor**) → null | 0.004 / 0.75 | 0.19 (unresp) | −0.23 | not expr. | null (anchor) | |
| NCI-H1573 | alt | R248L (homoz, hotspot) | missense LOF; GOF untested → null | 0.002 / 0.96 | 0.22 (unresp) | −0.72 | −1.38 | null-like | |
| SNU-423 | alt | splice c.376-2A>G (homoz) | splice-null → null | 0.001 / 0.50 | 0.14 (unresp) | −0.18 | 1.40 | null-like | |
| CFPAC-1 | alt | C242R (homoz, VAF 0.94) | missense LOF (DNE) → null-eq | 0.000 / 0.50 | 0.27 (unresp) | −0.60 | −0.78 | null-like | |
| HCT15 | alt | S241F + splice c.1101-2A>C (compound het) | missense+splice → null-like | −0.001 / 0.48 | 0.17 (unresp) | −0.16 | 1.33 | null-like | unphased; classed "truncating" in repo |
| AsPC-1 | alt | C135fs (hemizygous, VAF 1.0) | frameshift-null → null | −0.006 / 0.57 | 0.29 (unresp) | −0.60 | not expr. | null-like | |
| COLO 205 | alt | **in-frame** Y103_L111delinsL (homoz) | corrected: in-frame del, not fs → null (protein may be expressed) | −0.008 / 0.97 | 0.17 (unresp) | −0.67 | +0.23 | null-like | variant corrected; mRNA normal (not NMD) |
| NCI-H1792 | alt | splice c.672+1G>A (homoz) | splice-null → null | −0.009 / 0.58 | 0.17 (unresp) | −0.53 | not expr. | null-like (most negative b_p53, −0.067, within null spread) | |
| NCI-H2122 | alt | Q16L (VAF 0.73, functional) + C176F (VAF 0.19) | partial (Q16L functional) → up | −0.012 / 0.61 | 0.26 (unresp) | +0.43 | 4.21 | too little data (19% usable wells), high basal z 4.2 | **FLAG: lit partial vs data null-like** |
| SHP-77 | alt | C176W (homoz) | missense LOF → null-eq | −0.013 / 0.31 | 0.15 (unresp) | −0.40 | 0.19 | null-like (lowest missense b_p53, within null spread) | |
| NCI-H596 | alt | G245C (homoz, hotspot) | GOF untested → null | −0.016 / 0.33 | not measured | −0.18 | 1.27 | too little data (2% usable wells) | drops out of MG53 models |
| SW 1271 | alt | C277F (homoz, VAF 0.98) | missense LOF → null-eq | −0.035 / 0.63 | 0.04 (unresp) | +0.00 | 2.14 | null-like (low cells) | |
| NCI-H661 | alt | R158L + S215I (compound het) | missense LOF (partly ts) → null @37 | −0.036 / 0.44 | 0.20 (unresp) | −0.07 | 1.77 | null-like | **no TRIM72 → absent from all MG53 models** |
| SW 1088 | alt | R273C (homoz, hotspot) | GOF → non-canon | −0.048 / 0.65 | 0.26 (unresp) | −0.74 | 0.12 | null-like; lowest raw ind_P but offset-corrected ≈0 (low cells, 54% zero-TRIM72) | GOF invisible; drives several weak class signals |

Merged file: `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/scratchpad/p53mut/writer/per_line_merged.csv`.

**Data-vs-literature disagreements to note:** (1) **Hs 766T** is WT by genotype yet null-like in the data — the clearest discordance, and the literature (nutlin resistance, high CDKN2A mRNA) agrees the pathway is probably off. It is also the single most influential line in the `two_way` active set. (2) **SNU-1, A498, C32** are flagged "attenuated" by the overlay but are fully functional on inducibility. (3) The eight **hotspot-GOF** lines score null-like on canonical P as the overlay predicts for canonical targets; their reported gain-of-function is a non-canonical programme that P cannot see. (4) **NCI-H2122** is "partial" by literature (functional Q16L majority allele) but null-like in the data — though it has only 19% usable wells and a high basal p53 (z 4.2), so this is a weak data call. (5) The "residual" altered lines (robust core AN3 CA, BT-474; weaker MIA PaCa-2, J82, then HEC-1-A, HS-578T, NCI-H23, HOP62) are the nearest the data comes to "retained/up," at 5–31% of the WT-to-null gap — but the 8-line group is fragile (three rest on marginal calls, HOP62 is itself a null line, and SW 1088/NCI-H2122 outrank some of them on b_p53 yet are excluded).

---

## 3. What accounting for direction does to the MG53 results

### Downstream (MG53/TRIM72 → p53-program output)

- **Primary, data-defined, binary:** WT−altered −0.00183, two-way p 0.285, label p 0.304 [`genome_wide/tables/c_program_models.csv` row 0; fit on 17 WT / 30 altered]; covset none −0.00230 [row 4, 17/32]. Rebuilt from the export's non-cross-fitted P: −0.00177 (95% CI −0.0054 to +0.0018; label p 0.37; MDE80 0.0063) (recomputed).
- **Graded moderators (list-based/mixed), deconfounded within drug-dose:** responsiveness −0.0011 (p_perm 0.24), inducibility −0.0014 (0.16), basal −0.0014 (0.19) per SD; within genotype ≈0 (recomputed). Two specifications that first looked positive (naive drug-dose FE; genotype FE + moderator) were drug-dose-level confounds and vanish once each drug-dose × genotype cell gets its own moderator slope.
- **Functional groups (list-based):** responsive−unresponsive −0.0013 (CI −0.0055 to +0.0030, p 0.59); clean responsive-WT vs unresponsive-altered −0.0015 (p 0.54), closer to zero without SW 1088 (recomputed).
- **Mutation class (list-based):** missense-only − truncating +0.0040 (p 0.14), halving to +0.0020 without SW 1088; it rises to +0.0048 (p 0.037) only if the two compound lines (HCT15, AN3 CA) are reclassed as missense — a labelling choice, not a robust effect. Hotspot − other-altered +0.0070 (valid-permutation p ≈0.10, corrected from an earlier 0.042 that used an invalid null); single-line driven (SW 1088). P_down mirror −0.0079 (p ≈0.06) is the most consistent class hint but is a secondary outcome.
- **Leave-one-line-out:** no single line flips the sign of the binary diff (range −0.0025 to −0.0008); SW 1088 has the largest pull, C32 and A549 pull the other way (recomputed).
- **Multiplicity / power:** across ~24 tests the smallest multiplicity-corrected q is 0.54 (recomputed). The data exclude function-dependent slope changes of about 0.003/SD (genotype-free), 0.005–0.006 (within genotype) and 0.007–0.009 (group contrasts) at 80% power — all larger than the TRIM72 slopes themselves (b_WT 0.0009, b_alt 0.0026), so small modifications cannot be ruled out, but no grouping reveals a hidden effect.
- **One post-hoc lead (mixed basis, not established):** basal TP53 mRNA as a within-genotype moderator gives +0.0019/SD, p_perm 0.002, concentrated in altered lines (missense/high-mRNA mutants steeper than null/truncating); survives dropping SW 1088 and low-count lines but is Bonferroni-borderline across ~25–30 tests.

## 4. What 24 h mRNA can and cannot say here

- **No p53 protein.** Missense alleles typically stabilise and accumulate mutant p53 protein; a transcript snapshot cannot see that. MDM2/MDM4-mediated protein destabilisation in the "attenuated" WT lines, and any MG53–p53 protein-level interaction, are also invisible. TP53 mRNA is not p53 activity: truncating/splice lines have low mRNA (nonsense-mediated decay) regardless of protein behaviour.
- **Gain-of-function is off-target for program P.** Program P and the 21-gene panel measure canonical, WT-like p53 output. Reported GOF of the hotspot mutants (R248Q/W, R273H/C, G245S) acts through non-canonical programmes, so "null-like on P" for a GOF line is expected and does not contradict the overlay.
- **Dominant-negative on p63/p73** is not a canonical-P read-out and is not measured; and in the 30 lines with no WT allele there is no WT p53 for a mutant to poison.
- **Circularity.** Program P and the S2 drug-doses were selected using the binary WT/altered labels, so scoring lines on P biases altered lines toward "non-responsive" and WT lines toward "responsive." "No altered line up-regulates p53" is therefore partly built in — but the genotype-blind panel (zero altered-responsive discordants) corroborates it independently. An altered line that still responds would be strong evidence of retained function; a WT line that does not (Hs 766T) is good evidence of loss.

---

## 5. What the data leave open — further extraction/analysis of Tahoe-100M only (no lab work)

A concrete pipeline addition that would answer the direction question list-free on the full data on the user's machine:

1. **Label-free per-line p53 function with leave-one-line-out program derivation.** Re-derive program P from the full `genome_wide` tensor (`cache/r2_wl.npy`, not in RES) with each line's label left out of the P selection (or using the suggested data-defined grouping), then rescore every line's inducibility. **Answers:** removes the selection circularity, so a residual altered line or a below-null line could be identified without bias.
2. **Graded-function moderator in the primary model.** Refit the list-free primary test (`genome_wide` ddxg, P53PROG_UP_cf, covset gw) with the *same* placebo-exposure families and TP53-label permutation, but replace the binary label with (a) continuous per-line b_p53, or (b) three groups (WT / missense / truncating), with Hs 766T moved out of WT and the residual lines separated. **Answers:** whether per-line p53 direction, rather than the yes/no label, changes the −0.00183 slope. Report which three altered lines (NCI-H661, NCI-H2122, NCI-H596) remain excluded.
3. **A data-defined "missense-vs-null divergence" programme as a candidate mutant-p53 output.** Select genes induced *differently* in missense vs truncating lines across drug-doses, chosen without reference to TRIM72, then test TRIM72 against it. **Answers:** whether mutant-p53 gain-of-function or dominant-negative activity shows up at the mRNA level at all, and whether MG53 tracks it — the only mRNA-accessible handle on GOF.
4. **List-free between-line basal p53 level from `export/all_genes`.** Compute a per-line basal program-P level from `all_genes/plate_baselines` (per-line DMSO log2cpm of P's genes; on the user's machine, not in RES). **Answers:** a data-defined basal "p53 floor" per line, to replace the list-based basal measure and test it as a moderator.
5. **Confirm the basal-TP53-mRNA lead properly.** It is already in RES [`downstream_p53/tables/b_baseline_per_line.csv`, TP53_rel_reliable_plates] and gave p_perm 0.002 post-hoc; rerun it through the pipeline's label-permutation and placebo-gene machinery with multiplicity control. **Answers:** whether the one surviving within-altered signal is real.
6. **QC the low-count lines** (NCI-H596, NCI-H2122, SW 1088, NCI-H661, SW 1271) by recomputing from pooled counts per (drug-dose, line) to remove the negative-offset artifact before any per-mutant below-null call. **Answers:** whether the apparent "below-null" raw means are p53 or just counting floor.

Zygosity/LOH at TP53 hotspots cannot be obtained from Tahoe's metadata; whether per-cell reads could support allele-level calls is itself an unexamined extraction question.