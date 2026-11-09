---
symbol: "MIR193BHG"
type: "gene"
col: 15385
ensembl_id: "ENSG00000262454"
name: "MIR193b-365a host gene"
location: "16p13.12"
module: 24
arm: "+"
pooled_cpm: 29.84
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MIR193BHG

*MIR193b-365a host gene* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.82× (z +6.6, q 2e-08, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.336× (z -16.3, q 0e+00, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL8A]] (+0.63, fdr 7e-06), [[BRI3]] (+0.63, fdr 1e-05), [[MIR4458HG]] (+0.63, fdr 7e-06); moves opposite to [[TRIP12]] (-0.63, fdr 7e-06), [[EIF4G2]] (-0.58, fdr 1e-05), [[SRCAP]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[XRCC5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.6 | 2e-08 | 31/43 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.40×** | +5.1 | 8e-05 | 29/44 (J82, PANC-1, …) | top dose only |  |
| [[Artemether (drug)]] 5 µM |  | **1.55×** | +4.9 | 2e-04 | 27/44 (J82, PANC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.36×** | +4.7 | 4e-04 | 24/44 (CFPAC-1, A498, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.52×** | +4.6 | 4e-04 | 27/43 (A498, SW1417, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.023 | 18/44 (AsPC-1, A-427, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.031 | 19/45 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Artemether (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.031 | 16/44 (SW480, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.35×** | +3.3 | 0.059 | 17/44 (A-172, HS-578T, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.11 | 15/42 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.32× | +3.1 | 0.11 | 18/42 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.13 | 10/41 (CHP-212, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.336×** | -16.3 | 0e+00 | 38/43 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.293×** | -12.8 | 4e-35 | 38/44 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.355×** | -10.8 | 6e-25 | 23/25 (SW1417, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.421×** | -9.4 | 9e-19 | 34/44 (A549, SW1417, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -9.2 | 3e-18 | 34/43 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.423×** | -9.0 | 3e-17 | 35/39 (HepG2/C3A, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.446×** | -8.7 | 2e-16 | 30/38 (J82, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.447×** | -8.7 | 2e-16 | 34/44 (A549, SW1417, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.458×** | -8.1 | 3e-14 | 30/44 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.474×** | -8.1 | 3e-14 | 36/44 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -7.6 | 2e-12 | 34/44 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.509×** | -7.0 | 1e-10 | 31/42 (HS-578T, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.497×** | -7.0 | 1e-10 | 24/33 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.656×** | -6.2 | 2e-08 | 28/45 (HepG2/C3A, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -5.7 | 4e-07 | 28/45 (A-172, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -4.8 | 7e-05 | 28/40 (HEC-1-A, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.661×** | -4.5 | 2e-04 | 25/44 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.690×** | -3.9 | 0.002 | 24/44 (A498, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.704×** | -3.7 | 0.005 | 19/45 (J82, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.011 | 20/44 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.021 | 15/43 (NCI-H1792, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.84 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 71.7 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0772× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.0) |
| [[A549 (line)]] | wt | 83.1 | 1 (1 ⚠) | 9 (5 ⚠) | [[Trametinib (drug)]] 5 µM 3.60× (z +8.7) ⚠ cell-cycle shift, explains ~83% of this change | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 49.0 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -22.7) |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0397× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.127× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 0 | 9 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0765× (z -17.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[A-172 (line)]] | wt | 56.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.4) |
| [[Hs 766T (line)]] | wt | 51.5 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0932× (z -13.4) |
| [[HCT15 (line)]] | alt | 54.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.2) |
| [[A498 (line)]] | wt | 101 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -13.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 83.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0728× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0342× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.112× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.6) |
| [[SW48 (line)]] | wt | 26.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.9) |
| [[C32 (line)]] | wt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.0) |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.9) |
| [[SW480 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.0) |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -12.4) |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0776× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.8) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.4) |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL8A]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[BRI3]] | +0.63 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |
| [[BAHD1]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.62 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[RAB11FIP5]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[CAMLG]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[BCAS4]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RNF149]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KCTD7]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.58 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CEP41]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[HNRNPUL1]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RAB1B]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[EXTL2]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPK]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[POGLUT3]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FAM111A]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIR193BHG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XRCC5]] | C | MIR193BHG activity lowers XRCC5's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.41× higher at baseline in the lines without MIR193BHG | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent; its own permutation p |
| [[RPS10]] | C | MIR193BHG activity lowers RPS10's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without MIR193BHG | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent |
| [[RPS21]] | C | MIR193BHG activity lowers RPS21's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.54× higher at baseline in the lines without MIR193BHG | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-50.5, -25.2); signed map (-27.4, 7.4). **Vector** length 114, 31.4% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -6.8 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | -6.5 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -4.6 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.9 | -8.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.4 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.8 | -2.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MIR193b-365a host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.12 — chr16:14,301,389-14,331,067 (+) |
| Ensembl biotype | lncRNA |
| Also known as | lincNORS, HypERlnc |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51945) · Entrez [100129781](https://www.ncbi.nlm.nih.gov/gene/100129781) · Ensembl [ENSG00000262454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262454)

## Data

Gene col 15385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15385); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15385]; `tensor/DDL_lfc|DDL_z.npy` [15385]; `embed/gene_vectors.npy` [15385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15385 or target_col == 15385). Every well: [[MIR193BHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR193BHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
