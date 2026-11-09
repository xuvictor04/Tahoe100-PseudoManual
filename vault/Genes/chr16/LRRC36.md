---
symbol: "LRRC36"
type: "gene"
col: 8270
ensembl_id: "ENSG00000159708"
name: "leucine rich repeat containing 36"
location: "16q22.1"
module: 128
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 34
n_dd_up: 30
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# LRRC36

*leucine rich repeat containing 36* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.08× (z +22.3, q 0e+00, up in 11 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.575× (z -5.1, q 2e-04, down in 15 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA1B]] (+0.77, fdr 7e-06), [[CYS1]] (+0.70, fdr 7e-06), [[RFPL1S]] (+0.65, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[BASP1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.08×** | +22.3 | 0e+00 | 11/18 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.72×** | +15.0 | 0e+00 | 9/19 (SW480, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +12.9 | 7e-36 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +11.3 | 2e-27 | 19/24 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +9.5 | 2e-19 | 5/17 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.50×** | +8.9 | 6e-17 | 16/19 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +8.3 | 7e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.6 | 2e-12 | 3/8 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +5.5 | 3e-06 | 11/29 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.6 | 2e-04 | 1/10 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.89×** | +4.4 | 5e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.4 | 6e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.53×** | +4.1 | 0.001 | 7/24 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.6 | 0.011 | 1/13 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.015 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.015 | 3/26 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.022 | 4/15 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.022 | 3/21 (NCI-H2030, KATO III, …) | rises with dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.029 | 2/18 (NCI-H460, NCI-H1573) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.044 | 1/24 (NCI-H2030) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.044 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.055 | 4/16 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -5.1 | 2e-04 | 15/24 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -4.8 | 4e-04 | 14/23 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.680×** | -3.7 | 0.035 | 14/28 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -3.7 | 0.035 | 14/26 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.707×** | -3.3 | 0.089 | 10/21 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.713×** | -3.3 | 0.089 | 10/29 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Hesperidin (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.089 | 2/16 (NCI-H460, A549) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.719× | -3.1 | 0.15 | 6/19 (HOP62, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.5 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0578× (z -20.3) |
| [[PANC-1 (line)]] | alt | 7.70 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0667× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0104× (z -22.1) |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0347× (z -17.4) ⚠ toxic |
| [[A498 (line)]] | wt | 1.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +10.3) | — |
| [[A-172 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.848 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.956 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA1B]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CYS1]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[RFPL1S]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC00466]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[JPH3]] | +0.62 | +0.59 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[FBXO27]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ADGRB1]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[CDH23]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NOS1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NR5A2]] | +0.58 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ERICH6-AS1]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRC36's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ANKRD20A11P]] | B | ANKRD20A11P activity raises LRRC36's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without ANKRD20A11P | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[CNTNAP3]] | B | CNTNAP3 activity raises LRRC36's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without CNTNAP3 | 0.097 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[ANKRD20A21P]] | C | ANKRD20A21P activity raises LRRC36's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.44× lower at baseline in the lines without ANKRD20A21P | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BASP1-AS1]] | B | LRRC36 activity raises BASP1-AS1's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without LRRC36 | 0.052 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent |
| [[BVES-AS1]] | B | LRRC36 activity raises BVES-AS1's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without LRRC36 | 0.066 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent |
| [[ANKRD20A21P]] | C | LRRC36 activity raises ANKRD20A21P's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without LRRC36 | 0.079 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.6, 37.3); signed map (24.7, 25.2). **Vector** length 55.6, 12.2% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.8 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,326,798-67,385,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11004 |
| Matched by | ensembl_id |

UniProt [Q1X8D7](https://www.uniprot.org/uniprotkb/Q1X8D7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25615) · Entrez [55282](https://www.ncbi.nlm.nih.gov/gene/55282) · UniProt [Q1X8D7](https://www.uniprot.org/uniprotkb/Q1X8D7) · Ensembl [ENSG00000159708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159708)

## Data

Gene col 8270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8270); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8270]; `tensor/DDL_lfc|DDL_z.npy` [8270]; `embed/gene_vectors.npy` [8270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8270 or target_col == 8270). Every well: [[LRRC36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
