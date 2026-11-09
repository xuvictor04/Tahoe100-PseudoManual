---
symbol: "PRKCZ"
type: "gene"
col: 865
ensembl_id: "ENSG00000067606"
name: "protein kinase C zeta"
location: "1p36.33"
module: 2
arm: "+"
pooled_cpm: 43.04
n_lines_expressing: 40
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PRKCZ

*protein kinase C zeta* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.35× (z +5.5, q 3e-05, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.356× (z -26.3, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD4B]] (+0.66, fdr 1e-05), [[LIMK1]] (+0.65, fdr 1e-05), [[F11R]] (+0.62, fdr 1e-05); moves opposite to [[DECR1]] (-0.62, fdr 7e-05), [[ARHGAP24]] (-0.59, fdr 1e-05), [[RWDD2B]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[DBNDD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +5.5 | 3e-05 | 21/38 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.30×** | +4.4 | 0.003 | 17/38 (LS 180, SW48, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.005 | 16/38 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.013 | 15/38 (A498, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +3.7 | 0.029 | 17/38 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +3.5 | 0.039 | 14/38 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.3 | 0.083 | 18/38 (SW480, NCI-H2347, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.2 | 0.083 | 9/38 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.083 | 7/39 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.22× | +3.0 | 0.15 | 9/38 (SW480, SW48, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.356×** | -26.3 | 0e+00 | 38/38 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.419×** | -13.0 | 5e-36 | 32/38 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -11.3 | 3e-27 | 33/39 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -11.0 | 5e-26 | 35/38 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.652×** | -10.9 | 1e-25 | 27/38 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.484×** | -10.8 | 3e-25 | 32/38 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -10.1 | 6e-22 | 25/37 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -8.2 | 1e-14 | 27/39 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.619×** | -8.0 | 8e-14 | 21/35 (SW 900, SW48, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -7.5 | 5e-12 | 28/38 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.763×** | -6.9 | 3e-10 | 29/38 (HOP62, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.728×** | -5.7 | 5e-07 | 21/38 (HT-29, LS 180, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -5.4 | 3e-06 | 23/38 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.742×** | -5.4 | 3e-06 | 19/38 (HOP62, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.758×** | -5.0 | 2e-05 | 19/38 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.8 | 5e-05 | 21/38 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.628×** | -4.4 | 4e-04 | 18/38 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.763×** | -3.5 | 0.013 | 11/38 (HOP62, BT-474, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.028 | 9/38 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.1 | 0.053 | 12/38 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.063 | 11/38 (LS 180, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 81.0 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -21.2) |
| [[NCI-H1573 (line)]] | alt | 55.0 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -28.6) |
| [[C32 (line)]] | wt | 60.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.4) |
| [[PANC-1 (line)]] | alt | 37.5 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 87.6 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.2) ⚠ cell-cycle shift, explains ~61% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 55.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.0) |
| [[A549 (line)]] | wt | 28.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.4) |
| [[COLO 205 (line)]] | alt | 54.7 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +17.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.28× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.8) |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -14.3) |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0735× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.5) |
| [[SW1417 (line)]] | alt | 47.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -16.4) |
| [[SW480 (line)]] | alt | 54.0 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.25× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -21.3) |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -16.2) |
| [[LS 180 (line)]] | wt | 55.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -15.1) |
| [[RKO (line)]] | wt | 41.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -14.1) |
| [[SW48 (line)]] | wt | 62.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 48.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.5) |
| [[A498 (line)]] | wt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.8) |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0850× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -11.4) |
| [[BT-474 (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CFPAC-1 (line)]] | alt | 67.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.8) |
| [[HCT15 (line)]] | alt | 120 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.0) |
| [[J82 (line)]] | alt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.8) |
| [[KATO III (line)]] | alt | 55.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -16.4) |
| [[LoVo (line)]] | wt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0675× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.242× (z -10.3) |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 59.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -11.7) |
| [[A-172 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.82 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD4B]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[F11R]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 | pathway: Signaling by TGF-beta Receptor Complex; STRING 852 |
| [[GNAI2]] | +0.61 | +0.47 / +0.36 | both halves | 1e-04 | pathway: ESR-mediated signaling |
| [[MPND]] | +0.60 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[MAP3K9]] | +0.60 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[TNK2]] | +0.60 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[AP2A2]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[PWWP3A]] | +0.59 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[GDI1]] | +0.59 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MAST3]] | +0.58 | +0.57 / +0.21 | both halves | 7e-04 |  |
| [[TPD52L2]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.62 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[ARHGAP24]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RWDD2B]] | -0.58 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[LATS1]] | -0.58 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[MBNL3]] | -0.58 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[ZBED5]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ACOT2]] | -0.57 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[UQCRFS1]] | -0.56 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[RNF146]] | -0.56 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.56 | -0.57 / -0.20 | both halves | 7e-04 |  |
| [[ETAA1]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[WTAP]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRKCZ's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers PRKCZ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KIAA1671]] | C | KIAA1671 activity raises PRKCZ's level | lines that do not express KIAA1671 (3) vs lines expressing it (47) | 5.67× lower at baseline in the lines without KIAA1671 | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: SOX13, FZD5, PDCD6P1; maybe low, not absent |
| [[KLC3]] | C | KLC3 activity raises PRKCZ's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without KLC3 | 0.064 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent; co-absent with the target |
| [[MAP3K9]] | C | MAP3K9 activity raises PRKCZ's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 4.06× lower at baseline in the lines without MAP3K9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent; co-absent with the target |
| [[RTN4R]] | C | RTN4R activity raises PRKCZ's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without RTN4R | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DBNDD1]] | B | PRKCZ activity raises DBNDD1's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without PRKCZ | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; its own permutation p |
| [[CLN8]] | B | PRKCZ activity lowers CLN8's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.73× higher at baseline in the lines without PRKCZ | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; its own permutation p |
| [[SOCS5]] | B | PRKCZ activity lowers SOCS5's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.73× higher at baseline in the lines without PRKCZ | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C |
| [[RTN4R]] | B | PRKCZ activity raises RTN4R's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PRKCZ | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C |
| [[MAP3K9]] | C | PRKCZ activity raises MAP3K9's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 4.13× lower at baseline in the lines without PRKCZ | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.8, 2.6); signed map (-42.9, -6.1). **Vector** length 104, 26.9% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.3 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.3 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -26.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.1 | -13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:2,050,411-2,185,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCζ, PKC2 |
| Gene groups (HGNC) | Protein kinase C family |
| Reactome | 18 pathways, smallest: Estrogen-stimulated signaling through PRKCZ; TGF-beta receptor signaling in EMT (epithelial to mesenchymal transition); RHO GTPases Activate NADPH Oxidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05513](https://www.uniprot.org/uniprotkb/Q05513) (Protein kinase C zeta type):

> Calcium- and diacylglycerol-independent serine/threonine-protein kinase that functions in phosphatidylinositol 3-kinase (PI3K) pathway and mitogen-activated protein (MAP) kinase cascade, and is involved in NF-kappa-B activation, mitogenic signaling, cell proliferation, cell polarity, inflammatory response and maintenance of long-term potentiation (LTP). Upon lipopolysaccharide (LPS) treatment in macrophages, or following mitogenic stimuli, functions downstream of PI3K to activate …

**Summary**, from NCBI Gene [5590](https://www.ncbi.nlm.nih.gov/gene/5590):

> Protein kinase C (PKC) zeta is a member of the PKC family of serine/threonine kinases which are involved in a variety of cellular processes such as proliferation, differentiation and secretion. Unlike the classical PKC isoenzymes which are calcium-dependent, PKC zeta exhibits a kinase activity which is independent of calcium and diacylglycerol but not of phosphatidylserine. Furthermore, it is insensitive to typical PKC inhibitors and cannot be activated by phorbol ester. Unlike the classical …

**Accessions** — [HGNC:9412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9412) · Entrez [5590](https://www.ncbi.nlm.nih.gov/gene/5590) · UniProt [Q05513](https://www.uniprot.org/uniprotkb/Q05513) · Ensembl [ENSG00000067606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067606)

## Data

Gene col 865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 865); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 865]; `tensor/DDL_lfc|DDL_z.npy` [865]; `embed/gene_vectors.npy` [865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 865 or target_col == 865). Every well: [[PRKCZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
