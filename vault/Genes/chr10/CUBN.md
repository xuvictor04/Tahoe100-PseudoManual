---
symbol: "CUBN"
type: "gene"
col: 2862
ensembl_id: "ENSG00000107611"
name: "cubilin"
location: "10p13"
module: 80
arm: "+"
pooled_cpm: 31.02
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 22
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# CUBN

*cubilin* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 11.8× (z +36.4, q 0e+00, up in 25 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Retinoic acid (drug)]] 5 µM: 0.805× (z -4.6, q 0.003, down in 10 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSUH2]] (+0.69, fdr 7e-06), [[DPY19L2P2]] (+0.68, fdr 4e-05), [[BFSP1]] (+0.67, fdr 1e-05); moves opposite to [[LCMT1]] (-0.62, fdr 2e-05), [[PDPR2P]] (-0.59, fdr 7e-05), [[FLYWCH2]] (-0.58, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); 8 go from it, the strongest it → [[TRDMT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **11.8×** | +36.4 | 0e+00 | 25/26 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +18.7 | 0e+00 | 18/27 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +16.2 | 0e+00 | 16/26 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +15.3 | 0e+00 | 22/27 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +11.5 | 2e-28 | 18/27 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +10.9 | 1e-25 | 6/18 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +10.9 | 1e-25 | 12/20 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.1 | 3e-22 | 19/27 (HOP62, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +9.5 | 1e-19 | 18/26 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +9.4 | 2e-19 | 14/26 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +9.4 | 3e-19 | 11/22 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +9.3 | 9e-19 | 13/26 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.2 | 2e-11 | 11/26 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.9 | 3e-10 | 14/26 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 1e-04 | 7/26 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.6 | 1e-04 | 7/26 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.4 | 4e-04 | 10/27 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.74×** | +4.3 | 6e-04 | 6/25 (LOX-IMVI, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **0.805×** | -4.6 | 0.003 | 10/27 (C32, AN3 CA, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.588×** | -4.1 | 0.012 | 8/25 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.030 | 14/26 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.035 | 10/26 (C32, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.780×** | -3.5 | 0.046 | 2/26 (NCI-H661, SW480) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.054 | 8/26 (A-427, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.800× | -3.2 | 0.10 | 9/26 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Budesonide (drug)]] 5 µM |  | 0.810× | -3.1 | 0.10 | 3/26 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.745× | -3.1 | 0.10 | 5/27 (HOP62, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.812× | -3.1 | 0.10 | 13/26 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.803× | -3.1 | 0.10 | 11/27 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.813× | -3.1 | 0.10 | 10/26 (A-427, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.04 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 19.4× (z +18.5) | — |
| [[HS-578T (line)]] | alt | 9.06 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +14.3) | — |
| [[C32 (line)]] | wt | 74.4 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.14× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.196× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -9.2) |
| [[HOP62 (line)]] | alt | 13.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 16.6× (z +15.8) | — |
| [[A-172 (line)]] | wt | 9.09 | 2 | 0 | [[Auranofin (drug)]] 5 µM 30.2× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 30.3× (z +13.6) | [[Nimesulide (drug)]] 5 µM 0.107× (z -8.9) ⚠ toxic; unreliable plate only |
| [[NCI-H23 (line)]] | alt | 12.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 23.7× (z +20.1) | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 15.2× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 22.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 21.2× (z +16.5) | — |
| [[A-427 (line)]] | wt | 707 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.402× (z -8.8) |
| [[AN3 CA (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.9× (z +15.5) | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.116× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 8.69 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.4) | — |
| [[RKO (line)]] | wt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 50.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.5× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 8.67 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.7× (z +10.4) | — |
| [[A498 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSUH2]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DPY19L2P2]] | +0.68 | +0.80 / +0.42 | both halves | 4e-05 |  |
| [[BFSP1]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.66 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[DGKI]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[OXTR]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TRHDE]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FSIP1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.64 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | +0.64 | +0.68 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.62 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PDPR2P]] | -0.59 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[FLYWCH2]] | -0.58 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[WDR5]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MMS19]] | -0.56 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[SDHAP1]] | -0.56 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[PHKA2]] | -0.56 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC9]] | -0.55 | -0.63 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity lowers CUBN's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 3.02× higher at baseline in the lines without FER1L6 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CUBN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OXTR]] | B | OXTR activity lowers CUBN's level | lines that do not express OXTR (5) vs lines expressing it (45) | 3.31× higher at baseline in the lines without OXTR | 0.089 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; its own permutation p |
| [[SSUH2]] | C | SSUH2 activity lowers CUBN's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 11.83× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRDMT1]] | B | CUBN activity raises TRDMT1's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without CUBN | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[LINC01358]] | B | CUBN activity raises LINC01358's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without CUBN | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[DPY19L2P2]] | B | CUBN activity raises DPY19L2P2's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without CUBN | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[CFAP54]] | B | CUBN activity raises CFAP54's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without CUBN | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[UNC5C]] | B | CUBN activity raises UNC5C's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without CUBN | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[LINC00702]] | C | CUBN activity raises LINC00702's level | lines that do not express CUBN (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without CUBN | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent; co-absent with the target |
| [[DPY19L2P2-1]] | C | CUBN activity raises DPY19L2P2-1's level | lines that do not express CUBN (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without CUBN | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent; co-absent with the target |
| [[DPY19L2]] | C | CUBN activity raises DPY19L2's level | lines that do not express CUBN (21) vs lines expressing it (29) | 3.20× lower at baseline in the lines without CUBN | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.2, 15.9); signed map (27.4, 4.4). **Vector** length 66.5, 15.6% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +36.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +10.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.8 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cubilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:16,823,966-17,129,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IFCR, gp280; previously MGA1 |
| Reactome | 14 pathways, smallest: HDL clearance; Uptake of dietary cobalamins into enterocytes; Vitamin D (calciferol) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60494](https://www.uniprot.org/uniprotkb/O60494) (Cubilin):

> Endocytic receptor which plays a role in lipoprotein, vitamin and iron metabolism by facilitating their uptake. Acts together with LRP2 to mediate endocytosis of high-density lipoproteins, GC, hemoglobin, ALB, TF and SCGB1A1. Acts together with AMN to mediate endocytosis of the CBLIF-cobalamin complex. Binds to ALB, MB, Kappa and lambda-light chains, TF, hemoglobin, GC, SCGB1A1, APOA1, high density lipoprotein, and the CBLIF-cobalamin complex. Ligand binding requires calcium. Serves as …

**Summary**, from NCBI Gene [8029](https://www.ncbi.nlm.nih.gov/gene/8029):

> Cubilin (CUBN) acts as a receptor for intrinsic factor-vitamin B12 complexes. The role of receptor is supported by the presence of 27 CUB domains. Cubulin is located within the epithelium of intestine and kidney. Mutations in CUBN may play a role in autosomal recessive megaloblastic anemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2548) · Entrez [8029](https://www.ncbi.nlm.nih.gov/gene/8029) · UniProt [O60494](https://www.uniprot.org/uniprotkb/O60494) · Ensembl [ENSG00000107611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107611)

## Data

Gene col 2862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2862); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2862]; `tensor/DDL_lfc|DDL_z.npy` [2862]; `embed/gene_vectors.npy` [2862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2862 or target_col == 2862). Every well: [[CUBN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUBN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
