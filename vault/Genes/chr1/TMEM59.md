---
symbol: "TMEM59"
type: "gene"
col: 3776
ensembl_id: "ENSG00000116209"
name: "transmembrane protein 59"
location: "1p32.3"
module: 69
arm: "+"
pooled_cpm: 81.03
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TMEM59

*transmembrane protein 59* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +13.0, q 1e-35, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.353× (z -13.4, q 5e-38, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.422× (z -5.8, q 1e-06, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN1]] (+0.75, fdr 7e-06), [[ATOSA]] (+0.74, fdr 7e-06), [[ITM2B]] (+0.74, fdr 7e-06); moves opposite to [[EEFSEC]] (-0.69, fdr 8e-06), [[IFRD2]] (-0.67, fdr 7e-06), [[NAA15]] (-0.66, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +13.0 | 1e-35 | 47/49 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.1 | 1e-13 | 44/49 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.0 | 2e-13 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +7.7 | 1e-12 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.0 | 3e-10 | 33/41 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 36/50 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.4 | 6e-06 | 36/48 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +4.6 | 3e-04 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 28/48 (HOP62, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.007 | 32/48 (PANC-1, A-427, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.69×** | +3.6 | 0.020 | 29/47 (BT-474, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.32×** | +3.5 | 0.022 | 26/47 (PANC-1, LoVo, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.024 | 35/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.4 | 0.026 | 22/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.4 | 0.030 | 24/45 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.353×** | -13.4 | 5e-38 | 48/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.422×** | -5.8 | 1e-06 | 43/48 (HT-29, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.424×** | -5.8 | 1e-06 | 45/48 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -5.7 | 1e-06 | 33/48 (CFPAC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.429×** | -5.7 | 1e-06 | 40/48 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.459×** | -5.2 | 2e-05 | 40/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.491×** | -4.8 | 1e-04 | 39/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -3.7 | 0.013 | 27/48 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.11 | 29/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 89.9 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -15.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 79.4 | 4 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.344× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 96.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.40× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 53.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 47.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.16× (z +11.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -11.7) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 55.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -12.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -12.1) |
| [[HS-578T (line)]] | alt | 112 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -8.6) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 82.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -12.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 87.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.2) | — |
| [[A498 (line)]] | wt | 78.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -10.0) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 43.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.89× (z +8.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -9.7) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 92.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -9.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -10.4) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 62.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -9.2) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 122 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -11.5) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 71.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 100 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -11.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 69.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -11.5) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 72.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -9.0) |
| [[SW1417 (line)]] | alt | 114 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -13.9) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 65.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.216× (z -9.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 56.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 39.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -9.5) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 95.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -9.2) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -10.0) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -10.6) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -11.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 57.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.4) | — |
| [[LoVo (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -15.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 70.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 91.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0960× (z -9.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -9.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 91.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | +0.75 | +0.64 / +0.83 | both halves | 7e-06 |  |
| [[ATOSA]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[ITM2B]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | STRING 427 |
| [[USP33]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.72 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.71 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[PCMTD1]] | +0.71 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[HBP1]] | +0.71 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[GPBP1L1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ATF6B]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[YPEL5]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ELF2]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.69 | -0.58 / -0.73 | both halves | 8e-06 |  |
| [[IFRD2]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[NAA15]] | -0.66 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[CEP83]] | -0.66 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[DDX21]] | -0.66 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[TAF1B]] | -0.66 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[PUS1]] | -0.66 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[MPHOSPH6]] | -0.65 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[UTP14A]] | -0.65 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[POGK]] | -0.64 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[MGA]] | -0.64 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[PNO1]] | -0.64 | -0.67 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity lowers TMEM59's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.47× higher at baseline in the lines without TERT | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[TOP2A]] | B | TOP2A activity lowers TMEM59's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.1, -42.6); signed map (-14.3, 10.8). **Vector** length 139, 50.2% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.7 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.1 | -13.4 |
|  | [[EX229 (drug)]] 5 µM |  | -8.9 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.9 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.7 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.0 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,026,681-54,053,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC001; previously C1orf8 |
| Reactome | 5 pathways, smallest: RHOH GTPase cycle; RND1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXS4](https://www.uniprot.org/uniprotkb/Q9BXS4) (Transmembrane protein 59):

> Acts as a regulator of autophagy in response to S.aureus infection by promoting activation of LC3 (MAP1LC3A, MAP1LC3B or MAP1LC3C). Acts by interacting with ATG16L1, leading to promote a functional complex between LC3 and ATG16L1 and promoting LC3 lipidation and subsequent activation of autophagy. Modulates the O-glycosylation and complex N-glycosylation steps occurring during the Golgi maturation of several proteins such as APP, BACE1, SEAP or PRNP. Inhibits APP transport to the cell surface …

**Summary**, from NCBI Gene [9528](https://www.ncbi.nlm.nih.gov/gene/9528):

> This gene encodes a protein shown to regulate autophagy in response to bacterial infection. This protein may also regulate the retention of amyloid precursor protein (APP) in the Golgi apparatus through its control of APP glycosylation. Overexpression of this protein has been found to promote apoptosis in a glioma cell line. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:1239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1239) · Entrez [9528](https://www.ncbi.nlm.nih.gov/gene/9528) · UniProt [Q9BXS4](https://www.uniprot.org/uniprotkb/Q9BXS4) · Ensembl [ENSG00000116209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116209)

## Data

Gene col 3776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3776); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3776]; `tensor/DDL_lfc|DDL_z.npy` [3776]; `embed/gene_vectors.npy` [3776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3776 or target_col == 3776). Every well: [[TMEM59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
