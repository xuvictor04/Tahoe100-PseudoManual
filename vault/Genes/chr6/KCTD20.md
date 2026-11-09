---
symbol: "KCTD20"
type: "gene"
col: 3317
ensembl_id: "ENSG00000112078"
name: "potassium channel tetramerization domain containing 20"
location: "6p21.31"
module: 136
arm: "+"
pooled_cpm: 77.17
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# KCTD20

*potassium channel tetramerization domain containing 20* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.41× (z +4.9, q 3e-04, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 2.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.542× (z -24.0, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGA1]] (+0.60, fdr 1e-04), [[BMERB1]] (+0.59, fdr 3e-05), [[ARID3B]] (+0.59, fdr 3e-05); moves opposite to [[WDFY3]] (-0.58, fdr 1e-04), [[RAF1]] (-0.57, fdr 9e-05), [[GIPC2]] (-0.56, fdr 2e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 2.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.41×** | +4.9 | 3e-04 | 21/48 (SHP-77, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.9 | 3e-04 | 21/48 (RKO, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 7e-04 | 19/48 (J82, BT-474, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +4.5 | 8e-04 | 20/48 (SNU-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.5 | 8e-04 | 10/49 (KATO III, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.2 | 0.002 | 10/48 (BT-474, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.2 | 0.003 | 20/48 (HCT15, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.013 | 14/48 (KATO III, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.7 | 0.013 | 14/47 (SNU-1, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.16× | +3.7 | 0.013 | 15/48 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.3 | 0.047 | 15/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +3.3 | 0.047 | 8/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.064 | 7/49 (C-33 A, AN3 CA, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.071 | 3/48 (KATO III, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -24.0 | 0e+00 | 45/49 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -16.7 | 0e+00 | 37/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.773×** | -10.1 | 8e-22 | 30/48 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -10.0 | 1e-21 | 34/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.756×** | -7.2 | 9e-11 | 26/45 (CHP-212, A549, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.841× | -6.8 | 1e-09 | 21/48 (KATO III, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.791×** | -6.3 | 3e-08 | 28/47 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -5.9 | 3e-07 | 18/48 (HOP62, SW 1271, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.7 | 2e-04 | 24/48 (A-427, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.003 | 19/49 (NCI-H2347, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | 0.871× | -3.7 | 0.012 | 18/44 (HCT15, HOP62, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.897× | -3.5 | 0.023 | 9/48 (NCI-H460, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.5 | 0.023 | 0/50 | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.880× | -3.4 | 0.026 | 8/48 (SW 1088, A-427, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.881× | -3.4 | 0.027 | 14/49 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.028 | 11/48 (PANC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.920× | -3.2 | 0.042 | 4/48 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.904× | -3.1 | 0.068 | 11/49 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.814×** | -3.0 | 0.070 | 11/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.899× | -3.0 | 0.070 | 13/49 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.901× | -2.9 | 0.084 | 9/48 (NCI-H460, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.3 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -12.7) |
| [[A-427 (line)]] | wt | 83.6 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -17.5) |
| [[A498 (line)]] | wt | 42.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -17.0) |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 169 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.2) |
| [[HOP62 (line)]] | alt | 87.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 82.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -16.7) |
| [[HS-578T (line)]] | alt | 79.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -11.6) |
| [[LS 180 (line)]] | wt | 81.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 92.3 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.163× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.9) |
| [[PANC-1 (line)]] | alt | 100 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -20.4) |
| [[SNU-1 (line)]] | wt | 94.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.63× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change | [[Lonafarnib (drug)]] 5 µM 0.0866× (z -12.0) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.7) |
| [[A-172 (line)]] | wt | 72.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.2) |
| [[A549 (line)]] | wt | 64.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 58.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.9) |
| [[C32 (line)]] | wt | 62.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.4) |
| [[CHP-212 (line)]] | wt | 98.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0923× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.8) |
| [[HCT15 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -8.6) |
| [[HT-29 (line)]] | alt | 68.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.2) |
| [[KATO III (line)]] | alt | 76.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -13.1) |
| [[LoVo (line)]] | wt | 63.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 96.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.2) |
| [[RKO (line)]] | wt | 109 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -16.0) |
| [[SW 1271 (line)]] | alt | 111 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0573× (z -14.2) |
| [[SW480 (line)]] | alt | 77.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -12.9) |
| [[AN3 CA (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.8) |
| [[BT-474 (line)]] | alt | 59.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.9) |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.9) |
| [[H4 (line)]] | wt | 64.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 82.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 54.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.1) |
| [[SW1417 (line)]] | alt | 51.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGA1]] | +0.60 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[BMERB1]] | +0.59 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.59 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[MARK3]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZNF544]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TECPR1]] | +0.58 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[ARHGEF4]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[PFDN2]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ZXDC]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[GPRIN1]] | +0.56 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[CMIP]] | +0.55 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[MMP17]] | +0.55 | +0.38 / +0.50 | both halves | 7e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDFY3]] | -0.58 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RAF1]] | -0.57 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[GIPC2]] | -0.56 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[NNT]] | -0.55 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[LHFPL6]] | -0.55 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[NCOA2]] | -0.55 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[DYRK1A]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[DERA]] | -0.55 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[QTRT1]] | -0.54 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[FAS]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[NEIL1]] | -0.53 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[DECR1]] | -0.53 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KCTD20's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NNT]] | B | NNT activity lowers KCTD20's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.25× higher at baseline in the lines without NNT | 0.086 | ⚠ within organs, on part of the lines; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 2.9); signed map (-1.4, 47.7). **Vector** length 114, 28.5% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -24.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -16.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.8 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,442,767-36,491,143 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ108K11.3, MGC14254; previously C6orf69 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5Y7](https://www.uniprot.org/uniprotkb/Q7Z5Y7) (BTB/POZ domain-containing protein KCTD20):

> Promotes the phosphorylation of AKT family members.

**Summary**, from NCBI Gene [222658](https://www.ncbi.nlm.nih.gov/gene/222658):

> Predicted to enable identical protein binding activity. Predicted to be involved in positive regulation of phosphorylation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21052) · Entrez [222658](https://www.ncbi.nlm.nih.gov/gene/222658) · UniProt [Q7Z5Y7](https://www.uniprot.org/uniprotkb/Q7Z5Y7) · Ensembl [ENSG00000112078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112078)

## Data

Gene col 3317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3317); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3317]; `tensor/DDL_lfc|DDL_z.npy` [3317]; `embed/gene_vectors.npy` [3317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3317 or target_col == 3317). Every well: [[KCTD20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
