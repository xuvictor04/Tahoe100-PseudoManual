---
symbol: "C2orf69"
type: "gene"
col: 10893
ensembl_id: "ENSG00000178074"
name: "chromosome 2 open reading frame 69"
location: "2q33.1"
module: 22
arm: "+"
pooled_cpm: 29.23
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# C2orf69

*chromosome 2 open reading frame 69* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.96× (z +18.2, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +7.4, q 1e-11, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.784× (z -5.8, q 4e-06, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.215×, J82 0.313×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.409×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.163×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBF4]] (+0.67, fdr 1e-05), [[CCNF]] (+0.67, fdr 7e-06), [[OIP5]] (+0.67, fdr 7e-06); moves opposite to [[CDC37]] (-0.55, fdr 2e-05), [[RTF2]] (-0.53, fdr 1e-05), [[SUPT6H]] (-0.51, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM72D]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.96×** | +18.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.74×** | +17.0 | 0e+00 | 47/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.06×** | +12.1 | 1e-31 | 46/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.96×** | +11.3 | 2e-27 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.60×** | +11.2 | 4e-27 | 36/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +9.8 | 1e-20 | 33/46 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.87×** | +8.8 | 1e-16 | 38/47 (J82, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.57×** | +7.5 | 4e-12 | 36/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.4 | 1e-11 | 32/47 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.50×** | +6.8 | 6e-10 | 31/47 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.47×** | +6.5 | 4e-09 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.47×** | +6.5 | 4e-09 | 34/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 5e-09 | 31/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +6.0 | 6e-08 | 32/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.41×** | +5.7 | 3e-07 | 21/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.5 | 2e-04 | 22/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.5 | 2e-04 | 17/47 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.004 | 17/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.007 | 12/48 (A-172, NCI-H661, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.058 | 14/47 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.081 | 10/48 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.089 | 7/48 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10893.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.215×, J82 0.313×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.409×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.163×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -5.8 | 4e-06 | 23/48 (A-172, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.755×** | -4.7 | 6e-04 | 20/48 (H4, SW480, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.821× | -3.3 | 0.15 | 13/47 (A549, CHP-212, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | 0.826× | -3.2 | 0.15 | 12/48 (SW 1088, HCT15, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.826× | -3.2 | 0.15 | 6/47 (SW1417, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.832× | -3.1 | 0.18 | 12/48 (A-172, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.6 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.19× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 28.2 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +17.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 23.7 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.81× (z +12.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 30.7 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.02× (z +14.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 32.3 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +14.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 28.9 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.87× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 23.3 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 39.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.64× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 41.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 24.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.26× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 26.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +14.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 44.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.84× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 39.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.409× (z -11.5) |
| [[A-427 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.108× (z -10.0) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.163× (z -10.3) |
| [[HT-29 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.15× (z +8.8) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.13× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBF4]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CCNF]] | +0.67 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[OIP5]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NRF1]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[CDCA3]] | +0.64 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[PTTG1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[KIF18B]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[G2E3]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CDCA2]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[FAM72D]] | +0.62 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[PIF1]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC37]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RTF2]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SUPT6H]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[YME1L1]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TMCO1]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[INTS3]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[GTF2F1]] | -0.49 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[SPTLC1]] | -0.49 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM72D]] | C | FAM72D activity raises C2orf69's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.4, -57.2); signed map (-50.0, -40.6). **Vector** length 79.0, 17.8% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Phosphorylation of Emi1* (reactome, mean cos +0.50 to 5); *Activation of NIMA Kinases NEK9, NEK6, NEK7* (reactome, mean cos +0.51 to 4); *Golgi Cisternae Pericentriolar Stack Reorganization* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.4 | +12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.4 | +17.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +9.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.6 | +11.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.3 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +0.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | -4.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +2.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:199,911,293-199,955,935 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38973 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8R5](https://www.uniprot.org/uniprotkb/Q8N8R5) (Mitochondrial protein C2orf69):

> May play a role in the respiratory chain.

**Summary**, from NCBI Gene [205327](https://www.ncbi.nlm.nih.gov/gene/205327):

> Involved in oxidative phosphorylation. Located in mitochondrion. Implicated in combined oxidative phosphorylation deficiency 53. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26799) · Entrez [205327](https://www.ncbi.nlm.nih.gov/gene/205327) · UniProt [Q8N8R5](https://www.uniprot.org/uniprotkb/Q8N8R5) · Ensembl [ENSG00000178074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178074)

## Data

Gene col 10893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10893); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10893]; `tensor/DDL_lfc|DDL_z.npy` [10893]; `embed/gene_vectors.npy` [10893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10893 or target_col == 10893). Every well: [[C2orf69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
