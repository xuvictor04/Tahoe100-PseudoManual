---
symbol: "CRACDL"
type: "gene"
col: 12296
ensembl_id: "ENSG00000196872"
name: "CRACD like"
location: "2q11.2"
module: 44
arm: "+"
pooled_cpm: 11.06
n_lines_expressing: 25
n_dd_up: 22
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 25
direction_downstream: 43
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CRACDL

*CRACD like* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.49× (z +22.0, q 0e+00, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.590× (z -6.4, q 8e-08, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNA14]] (+0.69, fdr 7e-06), [[TM4SF4]] (+0.69, fdr 7e-06), [[TSPAN8]] (+0.68, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 43 go from it, the strongest it → [[MANSC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.49×** | +22.0 | 0e+00 | 8/20 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +18.6 | 0e+00 | 8/21 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +13.0 | 3e-36 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.8 | 2e-20 | 7/23 (A-172, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.6 | 1e-15 | 2/15 (LoVo, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.5 | 9e-09 | 3/22 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 3e-07 | 5/20 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.4 | 4e-06 | 1/22 (HEC-1-A) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.2 | 1e-05 | 6/23 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 5/23 (RKO, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 5e-04 | 4/23 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.0 | 0.004 | 3/13 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.007 | 7/23 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.7 | 0.008 | 4/23 (NCI-H2347, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.010 | 8/23 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.020 | 3/22 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.024 | 9/23 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.2 | 0.048 | 4/23 (RKO, LS 180, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.090 | 4/21 (COLO 205, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -6.4 | 8e-08 | 15/23 (LS 180, SHP-77, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -5.6 | 5e-06 | 16/23 (Panc 03.27, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -5.5 | 6e-06 | 17/23 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -4.6 | 7e-04 | 11/23 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -4.4 | 0.001 | 13/23 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.708×** | -4.2 | 0.003 | 18/23 (Hs 766T, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -3.8 | 0.014 | 16/22 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.743×** | -3.7 | 0.015 | 12/23 (HT-29, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.744×** | -3.5 | 0.025 | 14/22 (Hs 766T, A-427, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -3.4 | 0.041 | 11/23 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.599×** | -3.3 | 0.043 | 10/22 (LS 180, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.043 | 5/23 (SHP-77, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.768×** | -3.3 | 0.043 | 5/23 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -3.2 | 0.047 | 9/22 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.055 | 3/23 (AsPC-1, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0894× (z -16.2) |
| [[Hs 766T (line)]] | wt | 206 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -19.6) |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -12.3) |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0769× (z -11.6) |
| [[KATO III (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.126× (z -10.6) |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.202× (z -8.9) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.163× (z -8.8) |
| [[LoVo (line)]] | wt | 7.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +21.1) | — |
| [[A-172 (line)]] | wt | 8.42 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 6.64× (z +8.7) | — |
| [[A-427 (line)]] | wt | 8.11 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 7.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 5.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +10.4) | — |
| [[A498 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA14]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.68 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SYNPR-AS1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[NPNT]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PRSS51]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ABO]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRACDL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PCAT1]] | B | PCAT1 activity raises CRACDL's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.03× lower at baseline in the lines without PCAT1 | 0.029 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[UBE2Q2P13]] | B | UBE2Q2P13 activity lowers CRACDL's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 2.29× higher at baseline in the lines without UBE2Q2P13 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[MANSC1]] | B | MANSC1 activity raises CRACDL's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without MANSC1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises CRACDL's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without SPATA6L | 0.077 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises CRACDL's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.51× lower at baseline in the lines without ST6GALNAC1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises CRACDL's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.42× lower at baseline in the lines without FXYD3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[ABO]] | C | ABO activity raises CRACDL's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.73× lower at baseline in the lines without ABO | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK; co-absent with the target |
| [[SPINK5]] | C | SPINK5 activity raises CRACDL's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 3.03× lower at baseline in the lines without SPINK5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588; co-absent with the target |
| [[POU5F1B]] | C | POU5F1B activity raises CRACDL's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.01× lower at baseline in the lines without POU5F1B | 0.013 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent; co-absent with the target |
| [[ST8SIA6]] | C | ST8SIA6 activity raises CRACDL's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without ST8SIA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[PRKCH-AS1]] | C | PRKCH-AS1 activity raises CRACDL's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.11× lower at baseline in the lines without PRKCH-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 19, C 24. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANSC1]] | B | CRACDL activity raises MANSC1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without CRACDL | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[SLC44A3-AS1]] | B | CRACDL activity raises SLC44A3-AS1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without CRACDL | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PCAT1]] | B | CRACDL activity raises PCAT1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without CRACDL | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[SLC37A1]] | B | CRACDL activity raises SLC37A1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without CRACDL | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[SLC44A3]] | B | CRACDL activity raises SLC44A3's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without CRACDL | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PLAAT3]] | B | CRACDL activity raises PLAAT3's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without CRACDL | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PLAC8]] | B | CRACDL activity raises PLAC8's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.50× lower at baseline in the lines without CRACDL | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[SCIN]] | B | CRACDL activity raises SCIN's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without CRACDL | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[RSPH1]] | B | CRACDL activity raises RSPH1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without CRACDL | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[TNFRSF14-AS1]] | B | CRACDL activity raises TNFRSF14-AS1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without CRACDL | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PRSS51]] | B | CRACDL activity raises PRSS51's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without CRACDL | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[DTX4]] | B | CRACDL activity raises DTX4's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without CRACDL | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 52.2); signed map (61.4, 2.1). **Vector** length 66.1, 16.7% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.61 to 4); *Aspirin ADME* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +22.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CRACD like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,793,846-98,936,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC42367; previously C2orf55, KIAA1211L |
| Matched by | ensembl_id |

UniProt [Q6NV74](https://www.uniprot.org/uniprotkb/Q6NV74) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33454) · Entrez [343990](https://www.ncbi.nlm.nih.gov/gene/343990) · UniProt [Q6NV74](https://www.uniprot.org/uniprotkb/Q6NV74) · Ensembl [ENSG00000196872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196872)

## Data

Gene col 12296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12296); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12296]; `tensor/DDL_lfc|DDL_z.npy` [12296]; `embed/gene_vectors.npy` [12296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12296 or target_col == 12296). Every well: [[CRACDL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRACDL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
