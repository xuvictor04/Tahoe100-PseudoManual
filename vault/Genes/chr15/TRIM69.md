---
symbol: "TRIM69"
type: "gene"
col: 11746
ensembl_id: "ENSG00000185880"
name: "tripartite motif containing 69"
location: "15q21.1"
module: 32
arm: "+"
pooled_cpm: 18.21
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM69

*tripartite motif containing 69* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.72× (z +25.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.616× (z -8.0, q 6e-13, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.81, fdr 7e-06, ⚠ same locus), [[ZC3HAV1]] (+0.77, fdr 7e-06), [[IFIH1]] (+0.77, fdr 7e-06), [[PARP14]] (+0.76, fdr 7e-06); moves opposite to [[BRAT1]] (-0.64, fdr 4e-05), [[NBPF3]] (-0.63, fdr 3e-05), [[ACTR5]] (-0.63, fdr 4e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.72×** | +25.6 | 0e+00 | 43/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.46×** | +24.7 | 0e+00 | 44/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.3 | 3e-18 | 32/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.2 | 6e-18 | 30/46 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.9 | 9e-17 | 30/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +7.2 | 5e-11 | 28/47 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.2 | 5e-11 | 28/46 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 24/46 (J82, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 23/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 3e-05 | 23/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 9e-05 | 21/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 21/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 19/48 (A-172, J82, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 18/46 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 8e-04 | 17/47 (J82, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.616×** | -8.0 | 6e-13 | 29/48 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.652×** | -7.1 | 4e-10 | 28/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.578×** | -6.4 | 3e-08 | 25/45 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -5.7 | 2e-06 | 25/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.634×** | -5.3 | 1e-05 | 25/48 (C-33 A, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.638×** | -5.3 | 1e-05 | 25/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -5.1 | 3e-05 | 20/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 0.001 | 20/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -4.0 | 0.005 | 22/47 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.031 | 16/47 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -3.4 | 0.031 | 18/45 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.6 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.427× (z -8.5) |
| [[HS-578T (line)]] | alt | 10.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +17.4) | — |
| [[PANC-1 (line)]] | alt | 12.7 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +17.0) | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -11.2) |
| [[A498 (line)]] | wt | 15.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +23.1) | — |
| [[C32 (line)]] | wt | 11.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +18.5) | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0998× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 13.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +21.3) | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 79.5× (z +20.1) | — |
| [[NCI-H460 (line)]] | wt | 9.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.8× (z +30.7) | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +14.5) | [[Tofacitinib (citrate) (drug)]] 5 µM 0.355× (z -8.6) |
| [[COLO 205 (line)]] | alt | 39.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +15.8) | [[Tofacitinib (drug)]] 5 µM 0.280× (z -9.1) |
| [[Hs 766T (line)]] | wt | 16.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.187× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 21.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +20.4) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +15.8) | [[Tofacitinib (drug)]] 5 µM 0.317× (z -9.4) |
| [[HOP62 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.6) | — |
| [[KATO III (line)]] | alt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +12.9) | — |
| [[LoVo (line)]] | wt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +15.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.4) | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0710× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 6.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +13.4) | — |
| [[SW480 (line)]] | alt | 6.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +18.0) | — |
| [[AsPC-1 (line)]] | alt | 7.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.5) | — |
| [[H4 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 9.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 9.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 8.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +11.1) | — |
| [[RKO (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0761× (z -11.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 5.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.9) | — |
| [[SW48 (line)]] | wt | 8.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +10.4) | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.81 | +0.85 / +0.65 | both halves | 7e-06 | ⚠ same locus (17.7 kb: neighbours can correlate without regulation) |
| [[ZC3HAV1]] | +0.77 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[PARP14]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[DDX60]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[RIGI]] | +0.74 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[IFIT2]] | +0.74 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[SP140]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[IFIT3]] | +0.72 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[IFIT5]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[RNF213]] | +0.72 | +0.57 / +0.77 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[FBXO39]] | +0.72 | +0.54 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.63 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ACTR5]] | -0.63 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[FAM118A]] | -0.62 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[WRN]] | -0.62 | -0.66 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRIM69's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SALL1]] | B | SALL1 activity raises TRIM69's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 1.28× lower at baseline in the lines without SALL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM69's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity raises TRIM69's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 53.7); signed map (63.1, 32.2). **Vector** length 124, 33.9% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.56 to 56); *interferon gamma response* (hallmark, mean cos +0.58 to 60); *interferon* (control, mean cos +0.64 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.6 | +25.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +24.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +9.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.5 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.2 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -5.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.5 | -8.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.9 | -5.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.8 | -6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:44,728,988-44,767,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Trif, TRIMLESS; previously RNF36 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WT6](https://www.uniprot.org/uniprotkb/Q86WT6) (E3 ubiquitin-protein ligase TRIM69):

> E3 ubiquitin-protein ligase that plays an important role in antiviral immunity by restricting different viral infections including dengue virus or vesicular stomatitis indiana virus. Ubiquitinates viral proteins such as dengue virus NS3 thereby limiting infection. Also involved in antiviral immunity by mediating 'Lys-63'-linked ubiquitination of STING1, thereby promoting STING1 dimerization and downstream activation of cGAS-STING signaling. In addition, acts as a key mediator of type I …

**Summary**, from NCBI Gene [140691](https://www.ncbi.nlm.nih.gov/gene/140691):

> This gene encodes a member of the RING-B-box-coiled-coil (RBCC) family and encodes a protein with an N-terminal RING finger motif, a PRY domain and a C-terminal SPRY domain. The mouse ortholog of this gene is specifically expressed in germ cells at the round spermatid stages during spermatogenesis and, when overexpressed, induces apoptosis. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17857) · Entrez [140691](https://www.ncbi.nlm.nih.gov/gene/140691) · UniProt [Q86WT6](https://www.uniprot.org/uniprotkb/Q86WT6) · Ensembl [ENSG00000185880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185880)

## Data

Gene col 11746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11746); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11746]; `tensor/DDL_lfc|DDL_z.npy` [11746]; `embed/gene_vectors.npy` [11746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11746 or target_col == 11746). Every well: [[TRIM69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
