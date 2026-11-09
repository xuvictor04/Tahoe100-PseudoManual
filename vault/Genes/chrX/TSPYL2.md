---
symbol: "TSPYL2"
type: "gene"
col: 11502
ensembl_id: "ENSG00000184205"
name: "TSPY like 2"
location: "Xp11.22"
module: 41
arm: "+"
pooled_cpm: 36.2
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TSPYL2

*TSPY like 2* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +16.5, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.768× (z -3.9, q 0.039, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (H4 0.0775×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.204×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC9]] (+0.65, fdr 7e-06), [[CUL7]] (+0.60, fdr 4e-05), [[SAFB2]] (+0.59, fdr 2e-05); moves opposite to [[EIF4E]] (-0.54, fdr 1e-05), [[XPO5]] (-0.50, fdr 3e-05), [[NUP93]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ERO1B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +16.5 | 0e+00 | 40/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.87×** | +14.0 | 2e-42 | 44/47 (SNU-423, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +7.4 | 3e-11 | 37/47 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.9 | 8e-10 | 33/47 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +6.7 | 3e-09 | 37/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.9 | 3e-07 | 34/44 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +5.6 | 2e-06 | 30/47 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +5.3 | 7e-06 | 36/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 3e-04 | 26/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.4 | 5e-04 | 29/47 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.3 | 8e-04 | 26/47 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.6 | 0.016 | 3/48 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.018 | 22/47 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.020 | 21/47 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.022 | 24/47 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.032 | 20/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (H4 0.0775×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.768×** | -3.9 | 0.039 | 25/47 (NCI-H1792, SW 900, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.693×** | -3.8 | 0.039 | 32/47 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.723× | -3.4 | 0.12 | 25/47 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.794× | -3.3 | 0.12 | 22/47 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +22.1) | — |
| [[J82 (line)]] | alt | 27.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 36.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +17.2) | — |
| [[SW480 (line)]] | alt | 43.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.1) | — |
| [[C32 (line)]] | wt | 27.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +16.6) | — |
| [[A498 (line)]] | wt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[A549 (line)]] | wt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +18.2) | — |
| [[H4 (line)]] | wt | 47.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +11.6) | [[Ipatasertib (drug)]] 0.5 µM 0.0775× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 57.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +18.2) | — |
| [[Hs 766T (line)]] | wt | 52.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 26.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.22× (z +9.3) | — |
| [[LoVo (line)]] | wt | 24.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.19× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 63.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +17.0) | — |
| [[SW1417 (line)]] | alt | 43.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.4) | — |
| [[A-172 (line)]] | wt | 22.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.46× (z +14.2) | — |
| [[A-427 (line)]] | wt | 38.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 91.8 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.204× (z -8.7) |
| [[C-33 A (line)]] | alt | 40.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.10× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 59.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 64.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.27× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.4) | — |
| [[RKO (line)]] | wt | 21.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 177 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 45.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.9× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 69.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC9]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[CUL7]] | +0.60 | +0.63 / +0.42 | both halves | 4e-05 | pathway: IRE1alpha activates chaperones |
| [[SAFB2]] | +0.59 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[AKAP17A]] | +0.57 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[MORF4L2]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[KLHL15]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[POFUT2]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC35A2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LRIF1]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ARFIP2]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ARF4]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4E]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[XPO5]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NUP93]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[EMC8]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[KPNA1]] | -0.47 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PPP4R1]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ORC5]] | -0.47 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[MRTFB]] | -0.46 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[THAP12]] | -0.45 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[EPS15]] | -0.45 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[AAGAB]] | -0.45 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERO1B]] | C | ERO1B activity raises TSPYL2's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without ERO1B | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.9, -37.2); signed map (-50.1, 16.0). **Vector** length 116, 32.5% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +16.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.0 | +3.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.3 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TSPY like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,082,367-53,088,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SE20-4, HRIHFB2216, CTCL, DENTT, CDA1, CINAP, TSPX |
| Gene groups (HGNC) | TSPYL family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, P53_PATHWAY |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2G4](https://www.uniprot.org/uniprotkb/Q9H2G4) (Testis-specific Y-encoded-like protein 2):

> Part of the CASK/TBR1/TSPYL2 transcriptional complex which modulates gene expression in response to neuronal synaptic activity, probably by facilitating nucleosome assembly. May inhibit cell proliferation by inducing p53-dependent CDKN1A expression.

**Summary**, from NCBI Gene [64061](https://www.ncbi.nlm.nih.gov/gene/64061):

> This gene encodes a member of the testis-specific protein Y-encoded, TSPY-like/SET/nucleosome assembly protein-1 superfamily. The encoded protein is localized to the nucleolus where it functions in chromatin remodeling and as an inhibitor of cell-cycle progression. This protein may play a role in the suppression of tumor growth. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:24358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24358) · Entrez [64061](https://www.ncbi.nlm.nih.gov/gene/64061) · UniProt [Q9H2G4](https://www.uniprot.org/uniprotkb/Q9H2G4) · Ensembl [ENSG00000184205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184205)

## Data

Gene col 11502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11502); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11502]; `tensor/DDL_lfc|DDL_z.npy` [11502]; `embed/gene_vectors.npy` [11502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11502 or target_col == 11502). Every well: [[TSPYL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPYL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
