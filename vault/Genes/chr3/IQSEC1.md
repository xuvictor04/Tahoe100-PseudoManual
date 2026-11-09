---
symbol: "IQSEC1"
type: "gene"
col: 6917
ensembl_id: "ENSG00000144711"
name: "IQ motif and Sec7 domain ArfGEF 1"
location: "3p25.2"
module: 195
arm: "+"
pooled_cpm: 57.8
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# IQSEC1

*IQ motif and Sec7 domain ArfGEF 1* — 3p25.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 3.12×, A549 3.45×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 3.17×); [[Dinaciclib (drug)]] 5 µM in 1 line (HCT15 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -16.2, q 0e+00, down in 42 of 45 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.430× (z -13.3, q 4e-38, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAV2]] (+0.69, fdr 7e-06), [[CACNA1H]] (+0.65, fdr 1e-05), [[PLXND1]] (+0.62, fdr 2e-05); moves opposite to [[GTF2IRD2B]] (-0.59, fdr 4e-05), [[PAXIP1-AS2]] (-0.58, fdr 3e-05), [[GTF2IRD2]] (-0.56, fdr 1e-04).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM163]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PTPRU]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 3.12×, A549 3.45×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 3.17×); [[Dinaciclib (drug)]] 5 µM in 1 line (HCT15 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | 1.23× | +3.5 | 0.15 | 17/45 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.15 | 19/45 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.24× | +3.4 | 0.15 | 18/45 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.20× | +3.1 | 0.30 | 15/45 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.499×** | -16.2 | 0e+00 | 42/45 (HOP62, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -13.3 | 4e-38 | 40/45 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.583×** | -8.9 | 1e-16 | 34/45 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -8.1 | 5e-14 | 33/45 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -7.8 | 7e-13 | 34/46 (NCI-H23, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -7.0 | 2e-10 | 24/41 (NCI-H23, HOP62, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -6.7 | 2e-09 | 27/45 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -6.7 | 2e-09 | 28/44 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.677×** | -6.4 | 9e-09 | 26/45 (HOP62, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -6.2 | 3e-08 | 31/45 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.714×** | -5.5 | 1e-06 | 25/45 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -5.4 | 3e-06 | 25/47 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -4.9 | 3e-05 | 23/45 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.753×** | -4.7 | 1e-04 | 24/45 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -4.5 | 2e-04 | 21/46 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -4.3 | 7e-04 | 23/45 (HepG2/C3A, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.001 | 25/45 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.004 | 17/46 (A-172, CHP-212, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -3.8 | 0.004 | 19/45 (A-172, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -3.6 | 0.007 | 17/45 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.022 | 18/45 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.881× | -2.9 | 0.070 | 11/46 (Panc 03.27, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 199 | 0 | 16 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -18.5) |
| [[HOP62 (line)]] | alt | 155 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -25.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.138× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.0) |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.101× (z -14.0) |
| [[SW480 (line)]] | alt | 102 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 279 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 76.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0997× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.119× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 26.7 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.258× (z -12.2) |
| [[A549 (line)]] | wt | 44.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -9.7) |
| [[A-427 (line)]] | wt | 94.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 86.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.379× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -8.8) |
| [[SHP-77 (line)]] | alt | 210 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[AN3 CA (line)]] | alt | 99.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 49.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -10.4) |
| [[RKO (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -11.4) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 71.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -8.8) |
| [[C-33 A (line)]] | alt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.283× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 28.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -11.9) |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -14.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -15.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SW48 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAV2]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CACNA1H]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PLXND1]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SLCO4A1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[IGSF9B]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[NKD2]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.58 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[FIBCD1]] | +0.58 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[BMP8B]] | +0.57 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[ITPR3]] | +0.57 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PAXIP1-AS2]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[GTF2IRD2]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[PIGP]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[AHI1-DT]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[NSUN3]] | -0.52 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[RBM23]] | -0.51 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[RIPK2-DT]] | -0.51 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ZNF226]] | -0.51 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | -0.51 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.50 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[BORCS7]] | -0.49 | -0.56 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM163]] | B | TMEM163 activity raises IQSEC1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without TMEM163 | 0.051 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[RET]] | B | RET activity raises IQSEC1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without RET | 0.067 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[JAKMIP1]] | B | JAKMIP1 activity raises IQSEC1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without JAKMIP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[SORCS2]] | B | SORCS2 activity raises IQSEC1's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without SORCS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent |
| [[STRA6]] | B | STRA6 activity raises IQSEC1's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without STRA6 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRU]] | C | IQSEC1 activity raises PTPRU's level | lines that do not express IQSEC1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without IQSEC1 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: CD99, CLTCL1, ANO7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 2.8); signed map (-14.2, 42.3). **Vector** length 93.0, 22.0% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +7.5 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +7.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif and Sec7 domain ArfGEF 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,897,043-13,283,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0763, GEP100, BRAG2, ARF-GEP100 |
| Gene groups (HGNC) | IQSEC ARFGEF family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DN90](https://www.uniprot.org/uniprotkb/Q6DN90) (IQ motif and SEC7 domain-containing protein 1):

> Guanine nucleotide exchange factor for ARF1 and ARF6. Guanine nucleotide exchange factor activity is enhanced by lipid binding. Accelerates GTP binding by ARFs of all three classes. Guanine nucleotide exchange protein for ARF6, mediating internalization of beta-1 integrin. Involved in neuronal development (Probable). In neurons, plays a role in the control of vesicle formation by endocytoc cargo. Upon long term depression, interacts with GRIA2 and mediates the activation of ARF6 to internalize …

**Summary**, from NCBI Gene [9922](https://www.ncbi.nlm.nih.gov/gene/9922):

> Predicted to enable guanyl-nucleotide exchange factor activity and protein kinase binding activity. Predicted to be involved in several processes, including positive regulation of focal adhesion disassembly; positive regulation of keratinocyte migration; and regulation of postsynaptic neurotransmitter receptor internalization. Located in cytosol and nucleoplasm. Implicated in intellectual developmental disorder with short stature and behavioral abnormalities and lung adenocarcinoma. Biomarker …

**Accessions** — [HGNC:29112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29112) · Entrez [9922](https://www.ncbi.nlm.nih.gov/gene/9922) · UniProt [Q6DN90](https://www.uniprot.org/uniprotkb/Q6DN90) · Ensembl [ENSG00000144711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144711)

## Data

Gene col 6917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6917); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6917]; `tensor/DDL_lfc|DDL_z.npy` [6917]; `embed/gene_vectors.npy` [6917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6917 or target_col == 6917). Every well: [[IQSEC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQSEC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
