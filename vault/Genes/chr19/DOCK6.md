---
symbol: "DOCK6"
type: "gene"
col: 5025
ensembl_id: "ENSG00000130158"
name: "dedicator of cytokinesis 6"
location: "19p13.2"
module: 3
arm: "+"
pooled_cpm: 60.98
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DOCK6

*dedicator of cytokinesis 6* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 2.13× (z +13.8, q 2e-40, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.351× (z -26.7, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EML2]] (+0.69, fdr 7e-06), [[SYP]] (+0.66, fdr 3e-05), [[ARID3A]] (+0.65, fdr 1e-05); moves opposite to [[ADI1]] (-0.62, fdr 3e-05), [[COPS3]] (-0.62, fdr 3e-05), [[BCLAF1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[palbociclib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **2.13×** | +13.8 | 2e-40 | 48/49 (LS 180, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.82×** | +10.9 | 3e-25 | 43/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +8.6 | 2e-15 | 40/48 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +5.4 | 1e-05 | 26/48 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +4.4 | 0.001 | 27/49 (HOP62, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.3 | 0.002 | 17/48 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.017 | 22/47 (HOP62, H4, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +3.6 | 0.019 | 22/47 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.032 | 14/48 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 1.13× | +3.2 | 0.085 | 17/48 (LS 180, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.085 | 13/48 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.085 | 9/49 (SW 900, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.351×** | -26.7 | 0e+00 | 47/49 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -15.4 | 0e+00 | 35/48 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.415×** | -15.3 | 0e+00 | 45/48 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.454×** | -13.7 | 1e-40 | 32/40 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.587×** | -13.6 | 5e-40 | 46/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.490×** | -12.9 | 5e-36 | 40/48 (SW480, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -12.4 | 2e-33 | 41/48 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.511×** | -11.6 | 2e-29 | 37/47 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.501×** | -11.5 | 5e-29 | 38/44 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -11.0 | 4e-26 | 43/50 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -9.3 | 6e-19 | 40/49 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -8.1 | 3e-14 | 35/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.491×** | -6.7 | 8e-10 | 32/48 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.700×** | -6.1 | 5e-08 | 29/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.719×** | -5.9 | 1e-07 | 27/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.765×** | -4.8 | 5e-05 | 33/48 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -4.5 | 2e-04 | 25/48 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.026 | 18/49 (HOP62, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 76.1 | 4 (2 ⚠) | 9 (5 ⚠) | [[Selinexor (drug)]] 0.05 µM 3.52× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 98.9 | 1 | 11 (5 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.82× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -22.5) |
| [[HS-578T (line)]] | alt | 83.1 | 2 | 9 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.75× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -20.4) |
| [[A-172 (line)]] | wt | 77.0 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0380× (z -29.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 65.6 | 1 | 7 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.26× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -21.1) |
| [[PANC-1 (line)]] | alt | 38.0 | 2 (1 ⚠) | 6 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.75× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.5) |
| [[SW1417 (line)]] | alt | 82.4 | 1 | 7 (3 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.52× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -17.1) |
| [[Hs 766T (line)]] | wt | 81.0 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -20.2) |
| [[LoVo (line)]] | wt | 68.9 | 1 | 6 (3 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.13× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 96.0 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0565× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -23.0) |
| [[SNU-423 (line)]] | alt | 38.3 | 1 | 5 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 4.27× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 81.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -15.9) |
| [[HCT15 (line)]] | alt | 154 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 74.6 | 1 | 4 | [[Selinexor (drug)]] 0.05 µM 2.26× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.4) |
| [[A498 (line)]] | wt | 42.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.5) |
| [[A549 (line)]] | wt | 44.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.0) |
| [[BT-474 (line)]] | alt | 108 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.50× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 66.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.8) |
| [[RKO (line)]] | wt | 85.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 51.6 | 1 | 3 | [[Selinexor (drug)]] 0.05 µM 3.57× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.6) |
| [[SW480 (line)]] | alt | 85.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -19.9) |
| [[C32 (line)]] | wt | 39.0 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.9) |
| [[HT-29 (line)]] | alt | 49.6 | 1 | 2 | [[Selinexor (drug)]] 0.05 µM 2.59× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.3) |
| [[J82 (line)]] | alt | 36.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 49.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -15.3) |
| [[SW48 (line)]] | wt | 69.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.0) |
| [[A-427 (line)]] | wt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 88.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -22.2) |
| [[HOP62 (line)]] | alt | 43.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 71.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -18.7) |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0475× (z -13.9) |
| [[COLO 205 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -13.1) |
| [[KATO III (line)]] | alt | 39.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0462× (z -10.6) |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.9) |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML2]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SYP]] | +0.66 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ARID3A]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.64 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[SLC8B1]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GIPR]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[GGT7]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CNNM4]] | +0.62 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.61 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[BCORL1]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SS18L1]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[C19orf81]] | +0.61 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.62 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[COPS3]] | -0.62 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[BCLAF1]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.58 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[C5]] | -0.58 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ANXA2R-AS1]] | -0.58 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[NAALADL2]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[XNDC1N]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CRPPA]] | -0.56 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[DECR1]] | -0.56 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[HNRNPM]] | -0.55 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[FGD5-AS1]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DOCK6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[palbociclib (drug)]] 5 µM | C | DOCK6's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | DOCK6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.070 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.4, 1.4); signed map (-23.7, 22.6). **Vector** length 126, 40.4% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +10.0 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +9.7 | +8.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +8.4 | +13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +4.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +6.3 | +10.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.0 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.5 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.4 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -13.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -11.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,199,295-11,262,524 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1395, ZIR1 |
| Gene groups (HGNC) | DOCK family Rho GEFs |
| Reactome | 7 pathways, smallest: Factors involved in megakaryocyte development and platelet production; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HP0](https://www.uniprot.org/uniprotkb/Q96HP0) (Dedicator of cytokinesis protein 6):

> Acts as a guanine nucleotide exchange factor (GEF) for CDC42 and RAC1 small GTPases. Through its activation of CDC42 and RAC1, may regulate neurite outgrowth (By similarity).

**Summary**, from NCBI Gene [57572](https://www.ncbi.nlm.nih.gov/gene/57572):

> This gene encodes a member of the dedicator of cytokinesis (DOCK) family of atypical guanine nucleotide exchange factors. Guanine nucleotide exchange factors interact with small GTPases and are components of intracellular signaling networks. The encoded protein is a group C DOCK protein and plays a role in actin cytoskeletal reorganization by activating the Rho GTPases Cdc42 and Rac1. Mutations in this gene are associated with Adams-Oliver syndrome 2. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:19189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19189) · Entrez [57572](https://www.ncbi.nlm.nih.gov/gene/57572) · UniProt [Q96HP0](https://www.uniprot.org/uniprotkb/Q96HP0) · Ensembl [ENSG00000130158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130158)

## Data

Gene col 5025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5025); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5025]; `tensor/DDL_lfc|DDL_z.npy` [5025]; `embed/gene_vectors.npy` [5025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5025 or target_col == 5025). Every well: [[DOCK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
