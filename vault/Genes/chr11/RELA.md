---
symbol: "RELA"
type: "gene"
col: 10331
ensembl_id: "ENSG00000173039"
name: "RELA proto-oncogene, NF-kB subunit"
location: "11q13.1"
module: 189
arm: "+"
pooled_cpm: 55.93
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# RELA

*RELA proto-oncogene, NF-kB subunit* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.59× (z +6.9, q 3e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.478× (z -15.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNIP2]] (+0.64, fdr 1e-05), [[TNKS1BP1]] (+0.63, fdr 1e-05), [[DNAJB2]] (+0.63, fdr 1e-05); moves opposite to [[COP1]] (-0.57, fdr 2e-05), [[RBBP4]] (-0.52, fdr 3e-05), [[VSIG10]] (-0.52, fdr 4e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.9 | 3e-09 | 38/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +5.4 | 2e-05 | 28/48 (PANC-1, A-172, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +5.3 | 2e-05 | 27/47 (PANC-1, AsPC-1, …) | all doses, flat | composition shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.002 | 31/48 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +3.9 | 0.009 | 24/48 (PANC-1, AsPC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.009 | 24/47 (NCI-H460, A-427, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.013 | 21/47 (CFPAC-1, LoVo, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.076 | 16/47 (LOX-IMVI, SNU-1, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.099 | 16/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.478×** | -15.6 | 0e+00 | 43/48 (CFPAC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.428×** | -12.2 | 6e-32 | 36/42 (AsPC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.499×** | -10.4 | 5e-23 | 40/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -9.9 | 4e-21 | 43/48 (SNU-423, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.546×** | -8.7 | 3e-16 | 42/49 (HT-29, C32, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.714×** | -7.2 | 8e-11 | 39/48 (Hs 766T, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.680×** | -5.6 | 2e-06 | 38/47 (NCI-H23, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.769×** | -5.6 | 2e-06 | 33/48 (HS-578T, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.701×** | -5.3 | 6e-06 | 27/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.756×** | -4.2 | 0.002 | 25/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.757×** | -4.2 | 0.002 | 28/48 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.762×** | -4.1 | 0.002 | 27/48 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.003 | 23/47 (LS 180, A498, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.767×** | -4.0 | 0.003 | 25/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.038 | 23/48 (C32, A-172, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.042 | 17/48 (SW 1271, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.043 | 20/48 (C32, hTERT-HPNE, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.043 | 20/47 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.058 | 15/48 (NCI-H2347, BT-474, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.677×** | -3.1 | 0.058 | 14/48 (AN3 CA, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.061 | 15/48 (HT-29, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 78.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.2) |
| [[PANC-1 (line)]] | alt | 63.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.43× (z +9.8) | — |
| [[A-172 (line)]] | wt | 55.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 80.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.3) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.6) |
| [[BT-474 (line)]] | alt | 67.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 85.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -12.7) |
| [[HS-578T (line)]] | alt | 64.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.4) |
| [[HT-29 (line)]] | alt | 58.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 46.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 63.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.0) |
| [[SNU-423 (line)]] | alt | 67.4 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -18.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.5) |
| [[SW480 (line)]] | alt | 40.8 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.8) |
| [[C32 (line)]] | wt | 53.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 54.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 69.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 50.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.0) |
| [[A-427 (line)]] | wt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 82.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.5) |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 94.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.490× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 54.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.9) |
| [[KATO III (line)]] | alt | 50.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 49.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 43.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 99.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0805× (z -9.1) |
| [[SW1417 (line)]] | alt | 48.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.5) |
| [[SW48 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIP2]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 836 |
| [[TNKS1BP1]] | +0.63 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[DNAJB2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.63 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[MAP1S]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[RING1]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 | pathway: Cellular Senescence |
| [[ARVCF]] | +0.60 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[CREB3]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 | STRING 444 |
| [[TFE3]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[PIM3]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RBBP4]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[VSIG10]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NAA50]] | -0.52 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[WDR12]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ECHDC1]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[LINC03006-1]] | -0.50 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[UBE2L3]] | -0.50 | -0.37 / -0.37 | both halves | 8e-05 | pathway: Death Receptor Signaling |
| [[PAXBP1]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[IPO11]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF75D]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RELA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, -1.3); signed map (-4.3, 22.9). **Vector** length 117, 34.6% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +7.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +5.7 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.3 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.5 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.5 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +3.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.4 | -9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.5 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RELA proto-oncogene, NF-kB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,653,599-65,663,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p65; previously NFKB3 |
| Gene groups (HGNC) | NF-kappa B complex subunits; IPT domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 94 pathways, smallest: CLEC7A/inflammasome pathway; DEx/H-box helicases activate type I IFN and inflammatory cytokines production; IkBA variant leads to EDA-ID |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04206](https://www.uniprot.org/uniprotkb/Q04206) (Transcription factor p65):

> NF-kappa-B is a pleiotropic transcription factor present in almost all cell types and is the endpoint of a series of signal transduction events that are initiated by a vast array of stimuli related to many biological processes such as inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis. NF-kappa-B is a homo- or heterodimeric complex formed by the Rel-like domain-containing proteins RELA/p65, RELB, NFKB1/p105, NFKB1/p50, REL and NFKB2/p52. The heterodimeric …

**Summary**, from NCBI Gene [5970](https://www.ncbi.nlm.nih.gov/gene/5970):

> NF-kappa-B is a ubiquitous transcription factor involved in several biological processes. It is held in the cytoplasm in an inactive state by specific inhibitors. Upon degradation of the inhibitor, NF-kappa-B moves to the nucleus and activates transcription of specific genes. NF-kappa-B is composed of NFKB1 or NFKB2 bound to either REL, RELA, or RELB. The most abundant form of NF-kappa-B is NFKB1 complexed with the product of this gene, RELA. Four transcript variants encoding different isoforms …

**Accessions** — [HGNC:9955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9955) · Entrez [5970](https://www.ncbi.nlm.nih.gov/gene/5970) · UniProt [Q04206](https://www.uniprot.org/uniprotkb/Q04206) · Ensembl [ENSG00000173039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173039)

## Data

Gene col 10331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10331); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10331]; `tensor/DDL_lfc|DDL_z.npy` [10331]; `embed/gene_vectors.npy` [10331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10331 or target_col == 10331). Every well: [[RELA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
