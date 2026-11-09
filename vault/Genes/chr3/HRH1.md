---
symbol: "HRH1"
type: "gene"
col: 12253
ensembl_id: "ENSG00000196639"
name: "histamine receptor H1"
location: "3p25.3"
module: 151
arm: "+"
pooled_cpm: 119.77
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 44
n_dd_up_clean: 0
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 27
direction_downstream: 40
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# HRH1

*histamine receptor H1* — 3p25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 2.90×, NCI-H1573 2.66×; ⚠ cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -19.2, q 0e+00, down in 33 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK10]] (+0.63, fdr 7e-06), [[SYNJ2]] (+0.62, fdr 7e-06), [[F3]] (+0.62, fdr 9e-06); moves opposite to [[CHPT1]] (-0.58, fdr 1e-05), [[NCKAP1]] (-0.53, fdr 4e-05), [[DRAM2]] (-0.53, fdr 4e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 40 go from it, the strongest it → [[RUNX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 2.90×, NCI-H1573 2.66×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 0.05 µM |  | 1.23× | +3.3 | 0.29 | 9/38 (C32, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -19.2 | 0e+00 | 33/39 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.345×** | -19.2 | 0e+00 | 33/38 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.356×** | -18.6 | 0e+00 | 33/38 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.369×** | -18.0 | 0e+00 | 36/38 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.369×** | -17.9 | 0e+00 | 34/39 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -17.5 | 0e+00 | 31/33 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -15.3 | 0e+00 | 35/37 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.499×** | -12.5 | 4e-34 | 36/38 (C32, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -11.8 | 3e-30 | 28/35 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -11.2 | 2e-27 | 30/38 (H4, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -10.3 | 4e-23 | 31/40 (hTERT-HPNE, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.584×** | -9.7 | 1e-20 | 35/39 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -9.6 | 3e-20 | 30/38 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -9.0 | 8e-18 | 26/37 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.735×** | -7.8 | 2e-13 | 25/38 (Hs 766T, NCI-H1792, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.441×** | -7.7 | 4e-13 | 34/38 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -7.6 | 1e-12 | 25/38 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.746×** | -7.5 | 2e-12 | 24/38 (C32, HCT15, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -7.4 | 4e-12 | 27/38 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -7.4 | 4e-12 | 24/38 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -6.3 | 6e-09 | 30/38 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.544×** | -5.7 | 2e-07 | 25/39 (HOP62, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 335 | 0 | 19 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -20.6) |
| [[C32 (line)]] | wt | 124 | 0 | 15 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.194× (z -21.9) |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 15 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 347 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0803× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -18.9) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -17.5) |
| [[Hs 766T (line)]] | wt | 336 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -18.4) |
| [[J82 (line)]] | alt | 124 | 0 | 12 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -20.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 331 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -20.8) |
| [[AsPC-1 (line)]] | alt | 270 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -18.2) |
| [[PANC-1 (line)]] | alt | 104 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -16.1) |
| [[A-172 (line)]] | wt | 200 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -19.3) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -16.0) |
| [[H4 (line)]] | wt | 122 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0963× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.2) |
| [[LoVo (line)]] | wt | 266 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -20.0) |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 9 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -15.5) |
| [[HCT15 (line)]] | alt | 145 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.386× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 80.7 | 0 | 8 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.2) |
| [[HS-578T (line)]] | alt | 131 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.353× (z -11.1) |
| [[A549 (line)]] | wt | 162 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 65.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.138× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.283× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 70.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 72.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.255× (z -11.7) |
| [[LS 180 (line)]] | wt | 90.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.343× (z -8.8) |
| [[RKO (line)]] | wt | 98.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.3) |
| [[KATO III (line)]] | alt | 57.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.335× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 51.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -13.1) |
| [[SW 1271 (line)]] | alt | 249 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.7) |
| [[SW 900 (line)]] | alt | 120 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.1) |
| [[A498 (line)]] | wt | 56.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.291× (z -9.1) |
| [[SW1417 (line)]] | alt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.3) |
| [[SW48 (line)]] | wt | 181 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -14.4) |
| [[A-427 (line)]] | wt | 27.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK10]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[F3]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[BACH1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[IQCJ-SCHIP1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A51]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[C11orf91]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[EGFR]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | pathway: G alpha (q) signalling events |
| [[MARCHF3]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CYTOR]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[NCKAP1]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[DRAM2]] | -0.53 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[PAIP1]] | -0.51 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[RAVER2]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RBM33]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[FBXO9]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CNOT6L]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ANP32B]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ERBB2]] | -0.49 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[FHIP2A]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[HSF2]] | -0.49 | -0.46 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises HRH1's level | lines that do not express F3 (24) vs lines expressing it (26) | 3.52× lower at baseline in the lines without F3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[C11orf91]] | B | C11orf91 activity raises HRH1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 3.93× lower at baseline in the lines without C11orf91 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ADAMTS16]] | B | ADAMTS16 activity raises HRH1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 3.14× lower at baseline in the lines without ADAMTS16 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[RAI14]] | B | RAI14 activity raises HRH1's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without RAI14 | 0.016 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[VGF]] | B | VGF activity lowers HRH1's level | lines that do not express VGF (32) vs lines expressing it (18) | 1.70× higher at baseline in the lines without VGF | 0.023 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3 |
| [[ARHGAP22]] | B | ARHGAP22 activity raises HRH1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without ARHGAP22 | 0.027 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[KCNMA1]] | B | KCNMA1 activity raises HRH1's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without KCNMA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[VGF]] | B | VGF activity weakens HRH1's drug response | lines that do not express VGF (27) vs lines expressing it (12) | the lines without VGF respond 1.74× as strongly (z diff -2.52); strongest at Dinaciclib 0.05 µM: 0.41x vs 0.75x (z diff -4.5) | 0.039 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |
| [[EGFR]] | B | EGFR activity raises HRH1's level | lines that do not express EGFR (7) vs lines expressing it (43) | 3.22× lower at baseline in the lines without EGFR | 0.042 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[PTHLH]] | B | PTHLH activity raises HRH1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without PTHLH | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[ITGA2]] | B | ITGA2 activity raises HRH1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.54× lower at baseline in the lines without ITGA2 | 0.053 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[FAM107B]] | B | FAM107B activity raises HRH1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without FAM107B | 0.060 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 36, C 4. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1]] | B | HRH1 activity raises RUNX1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without HRH1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[MSANTD3]] | B | HRH1 activity raises MSANTD3's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without HRH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[SHB]] | B | HRH1 activity raises SHB's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without HRH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[HMGN2P46]] | B | HRH1 activity raises HMGN2P46's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.07× lower at baseline in the lines without HRH1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[CDCP1]] | B | HRH1 activity raises CDCP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.80× lower at baseline in the lines without HRH1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ITGA2]] | B | HRH1 activity raises ITGA2's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.39× lower at baseline in the lines without HRH1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[RHBDF2]] | B | HRH1 activity raises RHBDF2's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without HRH1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[VEGFC]] | B | HRH1 activity raises VEGFC's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without HRH1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ETS1]] | B | HRH1 activity raises ETS1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.84× lower at baseline in the lines without HRH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[SLC25A51]] | B | HRH1 activity raises SLC25A51's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without HRH1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[WFDC3]] | B | HRH1 activity raises WFDC3's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.26× lower at baseline in the lines without HRH1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[LUCAT1]] | B | HRH1 activity raises LUCAT1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.25× lower at baseline in the lines without HRH1 | 0.047 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.3, 1.4); signed map (4.1, 44.0). **Vector** length 116, 39.2% of its response variance represented; |z| ≥ 3 in 1,617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.9 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.3 | -15.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.4 | -12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -17.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -9.7 |

## What is on record

|  |  |
|---|---|
| Name | histamine receptor H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:11,137,093-11,263,557 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histamine receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 6 pathways, smallest: Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P35367](https://www.uniprot.org/uniprotkb/P35367) (Histamine H1 receptor):

> G protein-coupled receptor for histamine, a biogenic amine that functions as an immune modulator and a neurotransmitter. Through the H1 receptor, histamine mediates the contraction of smooth muscles and increases capillary permeability due to contraction of terminal venules. Also mediates neurotransmission in the central nervous system and thereby regulates circadian rhythms, emotional and locomotor activities as well as cognitive functions (By similarity).

**Summary**, from NCBI Gene [3269](https://www.ncbi.nlm.nih.gov/gene/3269):

> Histamine is a ubiquitous messenger molecule released from mast cells, enterochromaffin-like cells, and neurons. Its various actions are mediated by histamine receptors H1, H2, H3 and H4. The protein encoded by this gene is an integral membrane protein and belongs to the G protein-coupled receptor superfamily. It mediates the contraction of smooth muscles, the increase in capillary permeability due to contraction of terminal venules, the release of catecholamine from adrenal medulla, and …

**Accessions** — [HGNC:5182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5182) · Entrez [3269](https://www.ncbi.nlm.nih.gov/gene/3269) · UniProt [P35367](https://www.uniprot.org/uniprotkb/P35367) · Ensembl [ENSG00000196639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196639)

## Data

Gene col 12253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12253); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12253]; `tensor/DDL_lfc|DDL_z.npy` [12253]; `embed/gene_vectors.npy` [12253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12253 or target_col == 12253). Every well: [[HRH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HRH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
