---
symbol: "ANKMY1"
type: "gene"
col: 6888
ensembl_id: "ENSG00000144504"
name: "ankyrin repeat and MYND domain containing 1"
location: "2q37.3"
module: 17
arm: "-"
pooled_cpm: 47.74
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ANKMY1

*ankyrin repeat and MYND domain containing 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +8.1, q 2e-13, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.435× (z -13.6, q 3e-39, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.215× (z -9.3, q 2e-18, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPV1]] (+0.65, fdr 1e-05), [[HCG18]] (+0.62, fdr 1e-05), [[KCTD13]] (+0.61, fdr 1e-05); moves opposite to [[C1orf115]] (-0.63, fdr 1e-05), [[AMOT]] (-0.63, fdr 1e-05), [[TMEM14A]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDKN2B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.1 | 2e-13 | 40/48 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.006 | 28/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.016 | 26/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.34× | +3.4 | 0.11 | 23/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.21× | +3.1 | 0.25 | 15/48 (SW480, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.435×** | -13.6 | 3e-39 | 39/47 (A549, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.334×** | -12.6 | 4e-34 | 42/47 (LoVo, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.359×** | -11.8 | 7e-30 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.276×** | -11.2 | 5e-27 | 43/48 (LoVo, NCI-H23, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.215×** | -9.3 | 2e-18 | 45/49 (A-172, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -8.4 | 3e-15 | 34/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.508×** | -7.8 | 5e-13 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -7.7 | 8e-13 | 38/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.460×** | -6.8 | 9e-10 | 41/46 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.330×** | -6.7 | 1e-09 | 36/47 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -6.5 | 4e-09 | 38/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.576×** | -6.4 | 9e-09 | 31/47 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.585×** | -6.2 | 3e-08 | 32/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.713×** | -5.5 | 1e-06 | 33/48 (A-427, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.614×** | -5.2 | 8e-06 | 30/42 (C32, LoVo, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -4.3 | 6e-04 | 27/48 (SW 900, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.714×** | -3.9 | 0.003 | 27/48 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -3.9 | 0.003 | 26/48 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.721×** | -3.8 | 0.004 | 26/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.760×** | -3.2 | 0.037 | 21/48 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.0 | 0.058 | 20/48 (HepG2/C3A, COLO 205, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.704×** | -2.9 | 0.085 | 13/48 (Hs 766T, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **0.720×** | -2.9 | 0.090 | 21/47 (RKO, C-33 A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.9 | 0 | 11 (9 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -15.9) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -17.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -10.7) |
| [[A-172 (line)]] | wt | 73.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -10.9) |
| [[H4 (line)]] | wt | 116 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.181× (z -11.8) |
| [[LoVo (line)]] | wt | 62.1 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.144× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 71.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -10.2) |
| [[BT-474 (line)]] | alt | 60.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 78.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 48.1 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.314× (z -8.6) |
| [[A-427 (line)]] | wt | 43.6 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.153× (z -15.9) |
| [[A549 (line)]] | wt | 66.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.235× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 81.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -15.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.239× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 55.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -17.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -10.2) |
| [[HOP62 (line)]] | alt | 51.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 68.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 56.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.161× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 56.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 53.1 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.235× (z -9.1) |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 39.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 34.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.150× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 26.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0725× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.216× (z -8.6) |
| [[A498 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 65.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HepG2_C3A (line)]] | wt | 65.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 | same gene group |
| [[HCG18]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[KCTD13]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[QRICH2]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.60 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[WDR27]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[KCNJ14]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MYH3]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CDR2]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[UBAP1L]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[EXD3]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf115]] | -0.63 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[AMOT]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TMEM14A]] | -0.61 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SNX2]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[HPF1]] | -0.60 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HMGN3]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[TMEM9]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ALAD]] | -0.58 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[DIXDC1]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SLC44A2]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[FRRS1]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SKIC3]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2B]] | C | CDKN2B activity weakens ANKMY1's drug response | recorded loss-of-function mutation of CDKN2B in 13 lines vs 36 not recorded | the CDKN2B-altered lines respond 1.18× as strongly (z diff -1.16); strongest at Harringtonine 0.5 µM: 0.28x vs 0.58x (z diff -3.2) | 0.285 over the table, 0.094 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (17.6, 0.2); signed map (13.9, 1.6). **Vector** length 90.2, 26.7% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.3 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -4.5 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and MYND domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,479,422-240,569,209 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20499, ZMYND13 |
| Gene groups (HGNC) | Zinc fingers MYND-type; Ankyrin repeat domain containing; MORN repeat containing |
| Matched by | ensembl_id |

UniProt [Q9P2S6](https://www.uniprot.org/uniprotkb/Q9P2S6) carries no function annotation.

**Summary**, from NCBI Gene [51281](https://www.ncbi.nlm.nih.gov/gene/51281):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20987) · Entrez [51281](https://www.ncbi.nlm.nih.gov/gene/51281) · UniProt [Q9P2S6](https://www.uniprot.org/uniprotkb/Q9P2S6) · Ensembl [ENSG00000144504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144504)

## Data

Gene col 6888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6888); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6888]; `tensor/DDL_lfc|DDL_z.npy` [6888]; `embed/gene_vectors.npy` [6888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6888 or target_col == 6888). Every well: [[ANKMY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKMY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
