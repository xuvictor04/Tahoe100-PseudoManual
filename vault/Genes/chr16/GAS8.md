---
symbol: "GAS8"
type: "gene"
col: 6480
ensembl_id: "ENSG00000141013"
name: "dynein regulatory complex subunit 4"
location: "16q24.3"
module: 64
arm: "+"
pooled_cpm: 22.62
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# GAS8

*dynein regulatory complex subunit 4* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +19.0, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.588× (z -9.3, q 1e-17, down in 32 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.735× (z -5.4, q 1e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC7]] (+0.67, fdr 7e-06), [[CCDC102A]] (+0.64, fdr 7e-06), [[ZBTB4]] (+0.64, fdr 7e-06); moves opposite to [[ADAM10]] (-0.55, fdr 2e-05), [[PRDX4]] (-0.55, fdr 1e-05), [[TFRC]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DBNDD1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +19.0 | 0e+00 | 41/47 (NCI-H2030, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +8.8 | 3e-16 | 33/48 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.5 | 1e-11 | 27/46 (SW48, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.4 | 1e-11 | 28/47 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.9 | 6e-10 | 31/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.4 | 1e-08 | 28/47 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 2e-08 | 27/48 (HOP62, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 3e-05 | 16/48 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.011 | 14/48 (KATO III, CFPAC-1, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.055 | 4/47 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.055 | 5/48 (H4, HCT15, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.059 | 7/46 (LS 180, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -9.3 | 1e-17 | 32/45 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.684×** | -6.9 | 1e-09 | 24/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.684×** | -6.9 | 1e-09 | 27/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -5.4 | 1e-05 | 23/47 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.9 | 1e-04 | 24/48 (A-427, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.6 | 0.026 | 11/48 (C32, HEC-1-A, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.826×** | -3.5 | 0.038 | 13/48 (HS-578T, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.826×** | -3.5 | 0.038 | 17/47 (BT-474, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.833× | -3.3 | 0.058 | 16/47 (BT-474, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.058 | 15/47 (CFPAC-1, A549, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.837× | -3.1 | 0.098 | 9/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 31.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 18.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +19.5) | [[Vilanterol (drug)]] 0.5 µM 0.165× (z -9.1) |
| [[A498 (line)]] | wt | 19.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) | [[Imiquimod (maleate) (drug)]] 5 µM 0.320× (z -9.5) |
| [[C32 (line)]] | wt | 38.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 20.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0765× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Vilanterol (drug)]] 0.05 µM 0.0788× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.9) | [[AZD2858 (drug)]] 0.5 µM 0.0922× (z -8.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0474× (z -22.1) |
| [[SW480 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.6) | — |
| [[A549 (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0713× (z -11.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.5) | — |
| [[RKO (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.7) | — |
| [[A-172 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC7]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CCDC102A]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ZBTB4]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[BBS1]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 | pathway: Hedgehog 'on' state |
| [[ALOX12P2-1]] | +0.60 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[ZNF579]] | +0.59 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[STX4]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ZNF426]] | +0.58 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[SLC66A1]] | +0.57 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[GMEB2]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM10]] | -0.55 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PRDX4]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TFRC]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TSPO]] | -0.53 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[PALS2]] | -0.51 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[NME2]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[PIGF]] | -0.49 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[NHP2]] | -0.49 | -0.55 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DBNDD1]] | C | DBNDD1 activity raises GAS8's level | lines that do not express DBNDD1 (3) vs lines expressing it (47) | 2.50× lower at baseline in the lines without DBNDD1 | 0.009 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, RHBDF2, EIF4E3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.4, 9.8); signed map (9.1, -20.0). **Vector** length 93.1, 19.3% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +19.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.5 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +5.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:90,019,629-90,044,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GAS11, GAS8 |
| Gene groups (HGNC) | Dynein regulatory complex |
| Reactome | 3 pathways, smallest: Activation of SMO; Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [O95995](https://www.uniprot.org/uniprotkb/O95995) (Dynein regulatory complex subunit 4):

> Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes. Plays an important role in the assembly of the N-DRC linker (By similarity). Plays dual roles at both the primary (or non-motile) cilia to regulate hedgehog signaling and in motile cilia to coordinate cilia movement. Required for proper motile cilia functioning. Positively …

**Summary**, from NCBI Gene [2622](https://www.ncbi.nlm.nih.gov/gene/2622):

> This gene includes 11 exons spanning 25 kb and maps to a region of chromosome 16 that is sometimes deleted in breast and prostrate cancer. The second intron contains an apparently intronless gene, C16orf3, that is transcribed in the opposite orientation. This gene is a putative tumor suppressor gene. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:4166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4166) · Entrez [2622](https://www.ncbi.nlm.nih.gov/gene/2622) · UniProt [O95995](https://www.uniprot.org/uniprotkb/O95995) · Ensembl [ENSG00000141013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141013)

## Data

Gene col 6480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6480); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6480]; `tensor/DDL_lfc|DDL_z.npy` [6480]; `embed/gene_vectors.npy` [6480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6480 or target_col == 6480). Every well: [[GAS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
