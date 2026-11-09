---
symbol: "PLSCR1"
type: "gene"
col: 12001
ensembl_id: "ENSG00000188313"
name: "phospholipid scramblase 1"
location: "3q24"
module: 32
arm: "+"
pooled_cpm: 172.8
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 63
n_dd_up_clean: 2
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 53
direction_downstream: 71
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PLSCR1

*phospholipid scramblase 1* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.42× (z +4.5, q 0.004, up in 27 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 2.89×, A-172 2.35×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.62×, HS-578T 2.61×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.199× (z -21.2, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.93, fdr 7e-06), [[CMPK2]] (+0.92, fdr 7e-06), [[OAS3]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 71 go from it, the strongest it → [[CMPK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 2.89×, A-172 2.35×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.62×, HS-578T 2.61×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.5 | 0.004 | 27/39 (J82, HS-578T, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.080 | 23/40 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.5 | 0.080 | 26/40 (BT-474, C32, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.16 | 10/41 (PANC-1, LoVo, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.16 | 17/41 (SHP-77, BT-474, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.57× | +3.1 | 0.16 | 19/42 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.16 | 19/40 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.25× | +3.0 | 0.17 | 19/40 (KATO III, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 22 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.199×** | -21.2 | 0e+00 | 40/40 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.214×** | -20.2 | 0e+00 | 38/40 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.356×** | -19.1 | 0e+00 | 37/41 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.390×** | -17.4 | 0e+00 | 37/40 (RKO, SW1417, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.276×** | -16.9 | 0e+00 | 39/40 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.282×** | -16.6 | 0e+00 | 40/40 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.423×** | -15.9 | 0e+00 | 35/41 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.473×** | -13.9 | 8e-42 | 37/40 (HS-578T, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -13.3 | 1e-38 | 36/41 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.419×** | -11.4 | 3e-28 | 34/40 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.431×** | -11.0 | 2e-26 | 34/41 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.462×** | -10.1 | 3e-22 | 33/41 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.474×** | -9.8 | 8e-21 | 30/40 (LoVo, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.481×** | -9.6 | 4e-20 | 30/40 (LoVo, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.483×** | -9.0 | 1e-17 | 37/40 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.513×** | -8.7 | 1e-16 | 37/40 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -8.3 | 3e-15 | 36/40 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -8.1 | 2e-14 | 36/40 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 204 | 0 | 31 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -25.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0613× (z -20.7) |
| [[NCI-H23 (line)]] | alt | 200 | 0 | 28 (10 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0570× (z -22.8) |
| [[LoVo (line)]] | wt | 388 | 0 | 25 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0863× (z -26.2) |
| [[SNU-423 (line)]] | alt | 264 | 0 | 23 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -22.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -19.4) |
| [[A549 (line)]] | wt | 298 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -27.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0941× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 262 | 0 | 19 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.137× (z -21.3) |
| [[RPMI-7951 (line)]] | alt | 342 | 0 | 19 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.229× (z -21.4) |
| [[A-172 (line)]] | wt | 187 | 2 (2 ⚠) | 15 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.62× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.167× (z -17.9) |
| [[HS-578T (line)]] | alt | 199 | 2 (2 ⚠) | 15 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Panobinostat (drug)]] 5 µM 0.107× (z -20.9) |
| [[NCI-H1792 (line)]] | alt | 188 | 0 | 17 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.217× (z -19.7) |
| [[RKO (line)]] | wt | 182 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -30.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0826× (z -18.7) |
| [[A498 (line)]] | wt | 244 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -18.4) |
| [[NCI-H1573 (line)]] | alt | 145 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -23.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.260× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 13 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.241× (z -15.8) |
| [[SHP-77 (line)]] | alt | 131 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 227 | 0 | 13 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.183× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 332 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -17.2) |
| [[COLO 205 (line)]] | alt | 596 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -16.7) |
| [[KATO III (line)]] | alt | 356 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0832× (z -22.4) |
| [[CFPAC-1 (line)]] | alt | 209 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 535 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -19.4) |
| [[SW1417 (line)]] | alt | 316 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -27.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.153× (z -18.4) |
| [[CHP-212 (line)]] | wt | 147 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0857× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.124× (z -10.6) |
| [[Hs 766T (line)]] | wt | 119 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.280× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 199 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -20.0) |
| [[HT-29 (line)]] | alt | 145 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -23.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -14.9) |
| [[SW 900 (line)]] | alt | 123 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.228× (z -11.0) |
| [[J82 (line)]] | alt | 264 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.332× (z -13.9) |
| [[PANC-1 (line)]] | alt | 80.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -21.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.391× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 82.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -10.9) |
| [[LS 180 (line)]] | wt | 79.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -14.9) |
| [[SNU-1 (line)]] | wt | 84.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.182× (z -9.0) |
| [[C32 (line)]] | wt | 112 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.294× (z -13.7) |
| [[A-427 (line)]] | wt | 52.7 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.284× (z -10.3) |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.258× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 90.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -9.7) |
| [[AN3 CA (line)]] | alt | 39.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 38.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 29.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.93 | +0.86 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 661 |
| [[CMPK2]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 456 |
| [[OAS3]] | +0.91 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 691 |
| [[STAT1]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 723 |
| [[PARP9]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 713 |
| [[OAS2]] | +0.90 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 689 |
| [[OAS1]] | +0.89 | +0.84 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 727 |
| [[IFI44]] | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 713 |
| [[HERC6]] | +0.88 | +0.82 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 571 |
| [[SP110]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 418 |
| [[LAP3]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 426 |
| [[IFIT1]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 696 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 48, C 5. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises PLSCR1's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without SRMS | 2e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS1]] | B | OAS1 activity raises PLSCR1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises PLSCR1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without OAS2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[TRIM22]] | B | TRIM22 activity raises PLSCR1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.15× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFI44]] | B | IFI44 activity raises PLSCR1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.81× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[IFI27]] | B | IFI27 activity raises PLSCR1's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.74× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[MX1]] | B | MX1 activity raises PLSCR1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without MX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[FBXO39]] | B | FBXO39 activity raises PLSCR1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without FBXO39 | 0.002 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[CMPK2]] | B | CMPK2 activity raises PLSCR1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[RASGRP3]] | B | RASGRP3 activity raises PLSCR1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises PLSCR1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without SAMD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[SLC15A3]] | B | SLC15A3 activity raises PLSCR1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 67, C 4. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMPK2]] | B | PLSCR1 activity raises CMPK2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.88× lower at baseline in the lines without PLSCR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[HERC6]] | B | PLSCR1 activity raises HERC6's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.97× lower at baseline in the lines without PLSCR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[OAS3]] | B | PLSCR1 activity raises OAS3's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.58× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[PARP14]] | B | PLSCR1 activity raises PARP14's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[DTX3L]] | B | PLSCR1 activity raises DTX3L's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.71× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[TRIM14]] | B | PLSCR1 activity raises TRIM14's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without PLSCR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[TRIM25]] | B | PLSCR1 activity raises TRIM25's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without PLSCR1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[HELZ2]] | B | PLSCR1 activity raises HELZ2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without PLSCR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[UNC93B1]] | B | PLSCR1 activity raises UNC93B1's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PLSCR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[OAS2]] | B | PLSCR1 activity raises OAS2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 5.42× lower at baseline in the lines without PLSCR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[EIF2AK2]] | B | PLSCR1 activity raises EIF2AK2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without PLSCR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[SP110]] | B | PLSCR1 activity raises SP110's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.39× lower at baseline in the lines without PLSCR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.896). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 54.3); signed map (65.3, 32.1). **Vector** length 141, 61.3% of its response variance represented; |z| ≥ 3 in 1,880 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon Signaling* (reactome, mean cos +0.78 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.81 to 27); *Interferon gamma signaling* (reactome, mean cos +0.76 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.2 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.7 | -6.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.9 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.7 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | -1.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.9 | -19.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.1 | -15.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.4 | -11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.0 | -13.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.8 | -10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.9 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid scramblase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:146,515,180-146,544,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MMTRA1B |
| Gene groups (HGNC) | Phospholipid scramblases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, INTERFERON_ALPHA_RESPONSE, COMPLEMENT, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [O15162](https://www.uniprot.org/uniprotkb/O15162) (Phospholipid scramblase 1):

> Catalyzes calcium-induced ATP-independent rapid bidirectional and non-specific movement of phospholipids (lipid scrambling or lipid flip-flop) between the inner and outer leaflet of the plasma membrane resulting in collapse of the phospholipid asymmetry which leads to phosphatidylserine externalization on the cell surface. Mediates calcium-dependent phosphatidylserine externalization and apoptosis in neurons via its association with TRPC5 (By similarity). Also exhibits magnesium-dependent …

**Summary**, from NCBI Gene [5359](https://www.ncbi.nlm.nih.gov/gene/5359):

> This gene encodes a phospholipid scramblase family member. The encoded protein is involved in disruption of the asymmetrical distribution of phospholipids between the inner and outer leaflets of the plasma membrane, resulting in externalization of phosphatidylserine. This cell membrane disruption plays an important role in the blood coagulation cascade as well as macrophage clearing of apoptotic cells. The encoded protein has additionally been implicated in gene regulation and …

**Accessions** — [HGNC:9092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9092) · Entrez [5359](https://www.ncbi.nlm.nih.gov/gene/5359) · UniProt [O15162](https://www.uniprot.org/uniprotkb/O15162) · Ensembl [ENSG00000188313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188313)

## Data

Gene col 12001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12001); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12001]; `tensor/DDL_lfc|DDL_z.npy` [12001]; `embed/gene_vectors.npy` [12001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12001 or target_col == 12001). Every well: [[PLSCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLSCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
