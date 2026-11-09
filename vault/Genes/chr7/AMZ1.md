---
symbol: "AMZ1"
type: "gene"
col: 10547
ensembl_id: "ENSG00000174945"
name: "archaelysin family metallopeptidase 1"
location: "7p22.3"
module: 53
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# AMZ1

*archaelysin family metallopeptidase 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +18.6, q 0e+00, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.889× (z -6.9, q 3e-09, down in 10 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.726× (z -5.0, q 1e-04, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA1-AS1]] (+0.64, fdr 7e-06), [[LINC01500]] (+0.63, fdr 7e-06), [[RETREG1-AS1]] (+0.63, fdr 1e-05); moves opposite to [[ARMC8]] (-0.50, fdr 4e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ITGA11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +18.6 | 0e+00 | 34/43 (A549, A498, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.8 | 5e-35 | 8/14 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.1 | 7e-22 | 16/31 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +9.6 | 2e-19 | 22/43 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +8.7 | 4e-16 | 11/23 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +8.1 | 7e-14 | 22/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +7.0 | 3e-10 | 18/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 6e-06 | 9/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.0 | 5e-05 | 10/38 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 9/45 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 13/46 (A-172, SW480, …) | top dose only |  |
| [[Ciclopirox (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.009 | 4/44 (HS-578T, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.012 | 7/45 (C32, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.013 | 0/45 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.022 | 3/46 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.038 | 14/42 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.089 | 3/46 (COLO 205, C32, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -6.9 | 3e-09 | 10/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.726×** | -5.0 | 1e-04 | 18/46 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.863× | -3.4 | 0.096 | 9/47 (COLO 205, KATO III, …) | top dose only | low cells (technical?) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.096 | 8/47 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.096 | 7/46 (SW 900, SW 1271, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -3.3 | 0.096 | 6/38 (hTERT-HPNE, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.95 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +12.1) | [[Sunitinib (drug)]] 5 µM 0.0828× (z -9.6) ⚠ toxic · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -8.7) |
| [[A498 (line)]] | wt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 5.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 8.87 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.101× (z -10.4) ⚠ toxic · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.9) |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0850× (z -10.4) ⚠ cell-cycle shift, explains ~8% of this change |
| [[C32 (line)]] | wt | 4.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 5.97 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[HS-578T (line)]] | alt | 6.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.59 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0956× (z -8.6) |
| [[KATO III (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -8.6) |
| [[LoVo (line)]] | wt | 4.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.99 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.101× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 8.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.8× (z +17.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.55 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0887× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 5.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 7.99 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.121× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.38 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0970× (z -9.0) |
| [[SW1417 (line)]] | alt | 5.52 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0733× (z -10.5) |
| [[SW480 (line)]] | alt | 5.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA1-AS1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC01500]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RETREG1-AS1]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CFAP45]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[COL23A1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[AHRR]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.61 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[RYR1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CELF5]] | +0.60 | +0.46 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA11]] | B | ITGA11 activity raises AMZ1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 1.71× lower at baseline in the lines without ITGA11 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.1, -13.0); signed map (19.5, 17.2). **Vector** length 58.7, 7.48% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | archaelysin family metallopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,679,522-2,775,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1950 |
| Gene groups (HGNC) | M54 metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q400G9](https://www.uniprot.org/uniprotkb/Q400G9) (Archaemetzincin-1):

> Probable zinc metalloprotease.

**Summary**, from NCBI Gene [155185](https://www.ncbi.nlm.nih.gov/gene/155185):

> Predicted to enable metal ion binding activity and metallopeptidase activity. Predicted to be involved in proteolysis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22231) · Entrez [155185](https://www.ncbi.nlm.nih.gov/gene/155185) · UniProt [Q400G9](https://www.uniprot.org/uniprotkb/Q400G9) · Ensembl [ENSG00000174945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174945)

## Data

Gene col 10547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10547); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10547]; `tensor/DDL_lfc|DDL_z.npy` [10547]; `embed/gene_vectors.npy` [10547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10547 or target_col == 10547). Every well: [[AMZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
