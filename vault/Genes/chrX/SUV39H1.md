---
symbol: "SUV39H1"
type: "gene"
col: 2193
ensembl_id: "ENSG00000101945"
name: "SUV39H1 histone lysine methyltransferase"
location: "Xp11.23"
module: 22
arm: "+"
pooled_cpm: 4.26
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SUV39H1

*SUV39H1 histone lysine methyltransferase* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.68× (z +5.8, q 5e-06, up in 7 of 23 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.16× (z +4.8, q 4e-04, up in 10 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.632× (z -7.6, q 1e-11, down in 22 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HASPIN]] (+0.80, fdr 7e-06), [[PLK4]] (+0.78, fdr 7e-06), [[ZWINT]] (+0.77, fdr 7e-06); moves opposite to [[TALAM1]] (-0.68, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.68×** | +5.8 | 5e-06 | 7/23 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.1 | 9e-05 | 7/24 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +4.8 | 4e-04 | 10/41 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.47×** | +4.4 | 0.002 | 1/8 (CFPAC-1) | top dose only | composition shift |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +3.8 | 0.018 | 4/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.34×** | +3.3 | 0.087 | 10/41 (PANC-1, RKO, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.30× | +3.1 | 0.16 | 3/43 (SNU-423, NCI-H23, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.19 | 1/33 (NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -7.6 | 1e-11 | 22/34 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.668×** | -6.7 | 6e-09 | 27/43 (SW 900, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.600×** | -6.0 | 4e-07 | 21/42 (H4, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.616×** | -5.7 | 2e-06 | 17/43 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -5.0 | 8e-05 | 9/32 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.674×** | -4.4 | 0.001 | 15/42 (LoVo, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.778×** | -4.2 | 0.003 | 13/45 (A-172, RKO, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.613×** | -4.1 | 0.003 | 11/45 (HT-29, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.003 | 10/42 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -4.0 | 0.004 | 13/46 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.802×** | -3.7 | 0.013 | 10/44 (LoVo, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.736×** | -3.6 | 0.015 | 14/44 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.028 | 10/37 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.058 | 5/43 (NCI-H1792, SW480, …) | top dose only |  |
| [[Daidzin (drug)]] 0.05 µM |  | **0.748×** | -3.2 | 0.058 | 9/43 (COLO 205, BT-474, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.599×** | -3.1 | 0.058 | 2/41 (H4, HOP62) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.067 | 8/41 (Hs 766T, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.776×** | -3.0 | 0.090 | 9/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.776×** | -3.0 | 0.090 | 5/42 (LOX-IMVI, BT-474, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | **0.771×** | -2.9 | 0.091 | 5/41 (A549, SHP-77, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.02 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0638× (z -9.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0607× (z -9.4) |
| [[SW480 (line)]] | alt | 9.02 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0852× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 4.22 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -11.8) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HASPIN]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PLK4]] | +0.78 | +0.69 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ZWINT]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[EME1]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ERCC6L]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[SKA3]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[NCAPH]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[POLQ]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ZNF724]] | +0.74 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[E2F8]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM2]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF15]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.68 | -0.62 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises SUV39H1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without E2F8 | 0.018 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises SUV39H1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without CDC25A | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises SUV39H1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without TCF19 | 0.073 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises SUV39H1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without MYBL2 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SUV39H1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without AURKB | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -50.5); signed map (-44.2, -44.6). **Vector** length 68.9, 11.4% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.52 to 28); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.51 to 33); *Cell Cycle Checkpoints* (reactome, mean cos +0.51 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | +2.7 | +5.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +2.0 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.0 | +1.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.7 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.3 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SUV39H1 histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,695,554-48,709,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KMT1A; previously SUV39H |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing; eNoSC complex |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 6 pathways, smallest: SIRT1 negatively regulates rRNA expression; PKMTs methylate histone lysines; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O43463](https://www.uniprot.org/uniprotkb/O43463) (Histone-lysine N-methyltransferase SUV39H1):

> Histone methyltransferase that specifically mediates trimethylation of 'Lys-9' of histone H3 (H3K9me3) using monomethylated H3 'Lys-9' (H3K9me1) as substrate. Also weakly methylates histone H1 (in vitro). H3 'Lys-9' trimethylation represents a specific tag for epigenetic transcriptional repression by recruiting HP1 (CBX1, CBX3 and/or CBX5) proteins to methylated histones. Mainly functions in heterochromatin regions, thereby playing a central role in the establishment of constitutive …

**Summary**, from NCBI Gene [6839](https://www.ncbi.nlm.nih.gov/gene/6839):

> This gene encodes an evolutionarily-conserved protein containing an N-terminal chromodomain and a C-terminal SET domain. The encoded protein is a histone methyltransferase that trimethylates lysine 9 of histone H3, which results in transcriptional gene silencing. Loss of function of this gene disrupts heterochromatin formation and may cause chromosome instability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:11479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11479) · Entrez [6839](https://www.ncbi.nlm.nih.gov/gene/6839) · UniProt [O43463](https://www.uniprot.org/uniprotkb/O43463) · Ensembl [ENSG00000101945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101945)

## Data

Gene col 2193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2193); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2193]; `tensor/DDL_lfc|DDL_z.npy` [2193]; `embed/gene_vectors.npy` [2193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2193 or target_col == 2193). Every well: [[SUV39H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUV39H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
