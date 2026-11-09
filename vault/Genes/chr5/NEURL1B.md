---
symbol: "NEURL1B"
type: "gene"
col: 13197
ensembl_id: "ENSG00000214357"
name: "neuralized E3 ubiquitin protein ligase 1B"
location: "5q35.1"
module: 67
arm: "+"
pooled_cpm: 7.96
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 52
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NEURL1B

*neuralized E3 ubiquitin protein ligase 1B* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +9.2, q 3e-17, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.351× (z -18.4, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPSM2]] (+0.83, fdr 7e-06), [[CIT]] (+0.77, fdr 7e-06), [[CCNF]] (+0.76, fdr 7e-06); moves opposite to [[MCPH1]] (-0.62, fdr 3e-05), [[C1S]] (-0.60, fdr 5e-05), [[ZNF621]] (-0.60, fdr 3e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 52 go from it, the strongest it → [[CKAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +9.2 | 3e-17 | 21/40 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +8.9 | 1e-16 | 26/40 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +8.8 | 3e-16 | 24/40 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +7.3 | 4e-11 | 20/39 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.80×** | +6.7 | 2e-09 | 18/40 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +6.7 | 2e-09 | 19/40 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 1e-04 | 14/38 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.95×** | +4.4 | 1e-03 | 13/30 (NCI-H2347, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.003 | 13/40 (Hs 766T, H4, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.044 | 5/38 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.055 | 11/38 (hTERT-HPNE, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.11 | 11/39 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.11 | 3/38 (A498, AN3 CA, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.351×** | -18.4 | 0e+00 | 31/37 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.285×** | -15.1 | 0e+00 | 31/39 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.307×** | -14.7 | 0e+00 | 33/37 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.365×** | -12.6 | 4e-34 | 32/39 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.519×** | -11.5 | 1e-28 | 27/40 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.399×** | -11.5 | 2e-28 | 29/40 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.446×** | -10.1 | 6e-22 | 29/40 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -9.3 | 1e-18 | 20/37 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.492×** | -8.8 | 6e-17 | 25/39 (NCI-H2347, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.528×** | -7.5 | 3e-12 | 21/37 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.552×** | -7.4 | 6e-12 | 22/39 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -6.9 | 2e-10 | 19/33 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.578×** | -6.8 | 3e-10 | 18/37 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -6.5 | 4e-09 | 21/37 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -6.3 | 1e-08 | 19/39 (A-427, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.622×** | -5.9 | 1e-07 | 20/40 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 42.8 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0541× (z -22.2) |
| [[HEC-1-A (line)]] | alt | 8.20 | 0 | 5 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0503× (z -14.6) |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0317× (z -26.1) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.0) |
| [[A549 (line)]] | wt | 5.13 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0373× (z -17.2) |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -10.3) |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.7) |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.1) |
| [[LoVo (line)]] | wt | 8.44 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0806× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 2 | — | [[Selinexor (drug)]] 0.5 µM 0.0464× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 2.90 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0854× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 7.33 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0599× (z -10.2) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.5) |
| [[A498 (line)]] | wt | 4.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0879× (z -8.8) |
| [[J82 (line)]] | alt | 4.91 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.198× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0371× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0936× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 4.41 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.14× (z +8.7) ⚠ position not correctable | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0568× (z -8.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW48 (line)]] | wt | 9.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -10.9) |
| [[SW480 (line)]] | alt | 4.80 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.135× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPSM2]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[CIT]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 | same gene group |
| [[CCNF]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 | same gene group |
| [[PSRC1]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.74 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[CEP85]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TTK]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CCNA2]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NUF2]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KIFC1]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[C1S]] | -0.60 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ZNF621]] | -0.60 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.60 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[KRR1]] | -0.59 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEURL1B's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | C | PIMREG activity raises NEURL1B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 3.62× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[CDC20]] | C | CDC20 activity raises NEURL1B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.80× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ARHGEF26]] | C | ARHGEF26 activity raises NEURL1B's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without ARHGEF26 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |
| [[CDCA3]] | C | CDCA3 activity raises NEURL1B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.81× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 48, C 4. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CKAP2]] | B | NEURL1B activity raises CKAP2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.00× lower at baseline in the lines without NEURL1B | 0.010 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[CDKN3]] | B | NEURL1B activity raises CDKN3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without NEURL1B | 0.012 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIF1]] | B | NEURL1B activity raises PIF1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without NEURL1B | 0.012 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PTTG1]] | B | NEURL1B activity raises PTTG1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without NEURL1B | 0.013 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[TROAP]] | B | NEURL1B activity raises TROAP's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without NEURL1B | 0.026 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[CDCA3]] | B | NEURL1B activity raises CDCA3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without NEURL1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[KIF20A]] | B | NEURL1B activity raises KIF20A's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without NEURL1B | 0.035 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[INCENP]] | B | NEURL1B activity raises INCENP's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without NEURL1B | 0.037 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[GPSM2]] | B | NEURL1B activity raises GPSM2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NEURL1B | 0.038 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NEIL3]] | B | NEURL1B activity raises NEIL3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without NEURL1B | 0.040 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[GPSM2]] | B | NEURL1B activity strengthens GPSM2's drug response | lines that do not express NEURL1B (7) vs lines expressing it (41) | the lines without NEURL1B respond 0.72× as strongly (z diff +1.36); strongest at Idarubicin (hydrochloride) 5 µM: 0.79x vs 0.45x (z diff +5.6) | 0.045 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131; target measured in part of the lines; artifact flags |
| [[STAG3L5P-1]] | B | NEURL1B activity raises STAG3L5P-1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NEURL1B | 0.046 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.4, -55.5); signed map (-48.6, -40.2). **Vector** length 102, 23.5% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 12); *G2/M checkpoint* (hallmark, mean cos +0.61 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +8.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -15.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.2 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | neuralized E3 ubiquitin protein ligase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,641,263-172,691,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761M1511, Neur2, RNF67B |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 15 pathways, smallest: Constitutive Signaling by NOTCH1 HD Domain Mutants; Signaling by NOTCH1 HD Domain Mutants in Cancer; NOTCH2 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MQ27](https://www.uniprot.org/uniprotkb/A8MQ27) (E3 ubiquitin-protein ligase NEURL1B):

> E3 ubiquitin-protein ligase involved in regulation of the Notch pathway through influencing the stability and activity of several Notch ligands.

**Summary**, from NCBI Gene [54492](https://www.ncbi.nlm.nih.gov/gene/54492):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in ubiquitin-dependent endocytosis. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:35422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35422) · Entrez [54492](https://www.ncbi.nlm.nih.gov/gene/54492) · UniProt [A8MQ27](https://www.uniprot.org/uniprotkb/A8MQ27) · Ensembl [ENSG00000214357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214357)

## Data

Gene col 13197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13197); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13197]; `tensor/DDL_lfc|DDL_z.npy` [13197]; `embed/gene_vectors.npy` [13197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13197 or target_col == 13197). Every well: [[NEURL1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEURL1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
