---
symbol: "CFB"
type: "gene"
col: 14368
ensembl_id: "ENSG00000243649"
name: "complement factor B"
location: "6p21.33"
module: 70
arm: "+"
pooled_cpm: 34.56
n_lines_expressing: 30
n_dd_up: 44
n_dd_down: 31
n_dd_up_clean: 41
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 63
direction_downstream: 68
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CFB

*complement factor B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 3.35× (z +13.2, q 9e-37, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.407× (z -11.4, q 2e-27, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP1]] (+0.84, fdr 7e-06), [[EPSTI1]] (+0.82, fdr 7e-06), [[GBP2]] (+0.81, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 68 go from it, the strongest it → [[CARD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 3 with an alert ⚠; shown: the 15 strongest. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **3.35×** | +13.2 | 9e-37 | 25/28 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **4.28×** | +12.5 | 2e-33 | 25/26 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **3.71×** | +12.5 | 2e-33 | 26/28 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **4.16×** | +12.2 | 3e-32 | 24/27 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **3.28×** | +10.7 | 2e-24 | 26/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +10.6 | 4e-24 | 25/28 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **2.55×** | +10.2 | 2e-22 | 25/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **3.11×** | +10.1 | 3e-22 | 26/28 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.60×** | +8.5 | 9e-16 | 24/27 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.98×** | +8.4 | 3e-15 | 21/28 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.66×** | +8.0 | 5e-14 | 24/27 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.84×** | +7.4 | 9e-12 | 24/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **2.41×** | +7.2 | 2e-11 | 21/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.17×** | +6.9 | 2e-10 | 16/28 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +6.6 | 2e-09 | 24/28 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.407×** | -11.4 | 2e-27 | 22/28 (COLO 205, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.306×** | -10.6 | 7e-24 | 25/28 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.468×** | -9.6 | 1e-19 | 21/28 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.375×** | -8.8 | 2e-16 | 21/28 (HS-578T, COLO 205, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.409×** | -8.0 | 1e-13 | 21/28 (COLO 205, BT-474, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.432×** | -7.5 | 5e-12 | 22/28 (COLO 205, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.441×** | -7.3 | 2e-11 | 23/27 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.564×** | -7.3 | 2e-11 | 21/28 (BT-474, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.422×** | -7.1 | 9e-11 | 21/28 (COLO 205, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.467×** | -6.8 | 4e-10 | 20/28 (SW 900, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -6.4 | 6e-09 | 20/26 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.510×** | -6.0 | 7e-08 | 19/26 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.553×** | -5.3 | 4e-06 | 19/28 (BT-474, HS-578T, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.663×** | -5.2 | 7e-06 | 19/28 (CFPAC-1, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -5.1 | 2e-05 | 13/28 (A549, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.588×** | -4.6 | 1e-04 | 19/27 (HepG2/C3A, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 186 | 11 | 9 (5 ⚠) | [[Binimetinib (drug)]] 0.5 µM 3.75× (z +11.1) | [[Tofacitinib (drug)]] 5 µM 0.299× (z -11.9) |
| [[COLO 205 (line)]] | alt | 73.4 | 0 | 20 (9 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0290× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 15 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 4.75× (z +21.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 15.4× (z +13.5) | [[Tofacitinib (drug)]] 5 µM 0.149× (z -11.0) |
| [[A549 (line)]] | wt | 41.3 | 6 | 8 (5 ⚠) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 9.06× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0652× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.153× (z -8.9) |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 12 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0244× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 372 | 9 | 2 | [[Trametinib (drug)]] 0.5 µM 3.13× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.333× (z -8.8) |
| [[HS-578T (line)]] | alt | 120 | 4 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.73× (z +10.6) | [[Tofacitinib (drug)]] 5 µM 0.229× (z -12.1) |
| [[SW 900 (line)]] | alt | 114 | 5 | 6 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 4.26× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.0901× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 14.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 14.6× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 45.0 | 4 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.90× (z +9.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 7.78× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.250× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 68.4 | 3 | 3 | [[Tucidinostat (drug)]] 5 µM 4.94× (z +13.2) | [[Tofacitinib (drug)]] 5 µM 0.246× (z -11.7) |
| [[J82 (line)]] | alt | 75.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +19.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.3× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 88.3 | 4 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 7.15× (z +16.4) | [[Auranofin (drug)]] 5 µM 0.201× (z -9.5) |
| [[A-172 (line)]] | wt | 22.3 | 4 | 0 | [[Trametinib (drug)]] 5 µM 7.28× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 90.0 | 1 | 3 | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 5.70× (z +8.6) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.170× (z -9.1) |
| [[A498 (line)]] | wt | 14.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 7.65× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 47.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.18× (z +13.3) | [[Ixazomib citrate (drug)]] 5 µM 0.134× (z -10.4) |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.178× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 25.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP1]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[EPSTI1]] | +0.82 | +0.75 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP2]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GBP4]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TNFSF10]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[APOL1]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TRANK1]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[TMEM140]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[TRIM22]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[IDO1]] | +0.77 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CASP10]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 33, C 30. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises CFB's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without CTSS | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[WFDC2]] | B | WFDC2 activity raises CFB's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without WFDC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[UBA7]] | B | UBA7 activity raises CFB's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.67× lower at baseline in the lines without UBA7 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises CFB's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without XAF1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[IFIT3]] | B | IFIT3 activity raises CFB's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.93× lower at baseline in the lines without IFIT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[STEAP4]] | B | STEAP4 activity raises CFB's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without STEAP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[NOD2]] | B | NOD2 activity raises CFB's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 4.23× lower at baseline in the lines without NOD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CFB's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.20× lower at baseline in the lines without ELF3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LCN2]] | B | LCN2 activity raises CFB's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without LCN2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[TNS3]] | B | TNS3 activity raises CFB's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.85× lower at baseline in the lines without TNS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[RBM47]] | B | RBM47 activity raises CFB's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without RBM47 | 0.030 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[CD5L]] | B | CD5L activity raises CFB's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without CD5L | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 44, C 24. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD14]] | B | CFB activity raises CARD14's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without CFB | 0.008 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[MVP-DT]] | B | CFB activity raises MVP-DT's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without CFB | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[UBA7]] | B | CFB activity raises UBA7's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without CFB | 0.018 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[APOL6]] | B | CFB activity raises APOL6's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without CFB | 0.019 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[CTSS]] | B | CFB activity raises CTSS's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without CFB | 0.021 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[TMEM140]] | B | CFB activity raises TMEM140's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without CFB | 0.021 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[LCN2]] | B | CFB activity raises LCN2's level | lines that do not express CFB (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without CFB | 0.021 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[DDX60]] | B | CFB activity raises DDX60's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without CFB | 0.031 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[IFIT3]] | B | CFB activity raises IFIT3's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without CFB | 0.032 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[GBP3]] | B | CFB activity raises GBP3's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without CFB | 0.032 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[GBP1]] | B | CFB activity raises GBP1's level | lines that do not express CFB (20) vs lines expressing it (30) | 3.10× lower at baseline in the lines without CFB | 0.033 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[NUB1]] | B | CFB activity raises NUB1's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.31× lower at baseline in the lines without CFB | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.6, 50.5); signed map (61.1, 28.6). **Vector** length 141, 45.1% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.61 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.64 to 14); *Interferon gamma signaling* (reactome, mean cos +0.66 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +7.6 | +13.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +7.5 | +12.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +7.3 | +10.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +7.0 | +12.2 |
|  | [[Trametinib (drug)]] 5 µM |  | +6.8 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +10.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.5 | -11.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.8 | -7.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.8 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.8 | -9.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.5 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | complement factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,945,650-31,952,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2-Bf; previously BFD, BF |
| Gene groups (HGNC) | Serine proteases; Sushi domain containing; Complement system activation components |
| Hallmark sets | COAGULATION, XENOBIOTIC_METABOLISM, COMPLEMENT, KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE |
| Reactome | 6 pathways, smallest: Alternative complement activation; Activation of C3 and C5; Initial triggering of complement |
| Matched by | ensembl_id |

**Function**, from UniProt [P00751](https://www.uniprot.org/uniprotkb/P00751) (Complement factor B):

> Precursor of the catalytic component of the C3 and C5 convertase complexes of the alternative pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. The alternative complement pathway acts as an amplification loop that enhances other complement pathways (classical, lectin and GZMK) by promoting formation of additional C3 and C5 convertases. CFB is cleaved and activated by CFD to …

**Summary**, from NCBI Gene [629](https://www.ncbi.nlm.nih.gov/gene/629):

> This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alternative pathway C3 convertase. Bb is involved in the proliferation of preactivated B lymphocytes, …

**Accessions** — [HGNC:1037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1037) · Entrez [629](https://www.ncbi.nlm.nih.gov/gene/629) · UniProt [P00751](https://www.uniprot.org/uniprotkb/P00751) · Ensembl [ENSG00000243649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243649)

## Data

Gene col 14368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14368); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14368]; `tensor/DDL_lfc|DDL_z.npy` [14368]; `embed/gene_vectors.npy` [14368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14368 or target_col == 14368). Every well: [[CFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
