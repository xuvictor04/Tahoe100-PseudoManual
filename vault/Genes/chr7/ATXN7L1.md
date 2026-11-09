---
symbol: "ATXN7L1"
type: "gene"
col: 7120
ensembl_id: "ENSG00000146776"
name: "ataxin 7 like 1"
location: "7q22.3"
module: 143
arm: "+"
pooled_cpm: 102.39
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ATXN7L1

*ataxin 7 like 1* — 7q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 7.84×, J82 3.06×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.514× (z -11.6, q 2e-28, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRADD]] (+0.70, fdr 9e-06), [[BAZ2B]] (+0.64, fdr 2e-05), [[FOXP1]] (+0.63, fdr 1e-05); moves opposite to [[POGLUT2]] (-0.66, fdr 1e-05), [[PDZD7]] (-0.66, fdr 1e-05), [[SDHAP4]] (-0.66, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7120.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 7.84×, J82 3.06×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 10.2×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.21× | +3.3 | 0.30 | 23/48 (A-427, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.30 | 24/47 (C32, SNU-423, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.30 | 21/49 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.514×** | -11.6 | 2e-28 | 47/49 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.462×** | -9.2 | 1e-17 | 39/47 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.481×** | -9.0 | 3e-17 | 39/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.248×** | -9.0 | 3e-17 | 46/49 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.491×** | -8.8 | 2e-16 | 39/49 (RKO, SHP-77, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.493×** | -8.7 | 3e-16 | 39/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.480×** | -8.4 | 4e-15 | 34/45 (NCI-H23, SNU-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.560×** | -7.1 | 6e-11 | 35/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.549×** | -7.1 | 7e-11 | 27/43 (SW48, LS 180, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.334×** | -7.1 | 9e-11 | 39/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.565×** | -7.1 | 9e-11 | 37/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.600×** | -6.3 | 1e-08 | 34/48 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.420×** | -5.6 | 1e-06 | 28/38 (SK-MEL-2, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -5.4 | 3e-06 | 30/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -4.5 | 2e-04 | 27/47 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -4.5 | 3e-04 | 27/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -4.4 | 4e-04 | 32/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -4.1 | 0.001 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -4.0 | 0.001 | 28/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.551×** | -3.8 | 0.003 | 30/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.003 | 28/48 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.689×** | -3.3 | 0.021 | 25/48 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.040 | 20/49 (LS 180, SW480, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.780×** | -3.1 | 0.040 | 19/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.774×** | -3.0 | 0.043 | 24/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.781×** | -2.9 | 0.058 | 19/49 (J82, HCT15, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -2.9 | 0.068 | 22/48 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 200 | 0 | 13 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -17.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.9) |
| [[KATO III (line)]] | alt | 152 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -16.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 93.0 | 0 | 10 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0801× (z -20.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 0 | 8 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -14.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.7) |
| [[COLO 205 (line)]] | alt | 162 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -14.8) |
| [[PANC-1 (line)]] | alt | 74.5 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -15.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.3) |
| [[SNU-1 (line)]] | wt | 126 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 182 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.249× (z -10.2) |
| [[C32 (line)]] | wt | 241 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -12.7) |
| [[RKO (line)]] | wt | 118 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0636× (z -22.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.8) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.0) |
| [[A-172 (line)]] | wt | 26.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +16.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 79.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 175 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 81.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.4) |
| [[LS 180 (line)]] | wt | 171 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -11.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.8) |
| [[AN3 CA (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -11.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -14.1) |
| [[J82 (line)]] | alt | 61.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.366× (z -9.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 86.7 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.140× (z -8.9) |
| [[SW1417 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.5) |
| [[A549 (line)]] | wt | 77.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 92.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.117× (z -9.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 88.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -13.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.292× (z -9.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -12.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0865× (z -9.9) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 119 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.110× (z -9.4) |
| [[A498 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRADD]] | +0.70 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[BAZ2B]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[FOXP1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[JPX]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TTC27]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.61 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[EPC2]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[SLC25A13]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[BPTF]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[BRAF]] | +0.59 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ST7L]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RGS5]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.66 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[PDZD7]] | -0.66 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.66 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[IDH2]] | -0.62 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ZNF710-AS1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GET1]] | -0.58 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[SGTB]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[P3H1]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[CDS2]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -8.1); signed map (14.8, -12.3). **Vector** length 107, 38.9% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.9 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.2 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.6 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.0 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -3.9 | -7.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 7 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,604,772-105,876,599 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1218, MGC33190; previously ATXN7L4 |
| Gene groups (HGNC) | Ataxin 7 family |
| Matched by | ensembl_id |

UniProt [Q9ULK2](https://www.uniprot.org/uniprotkb/Q9ULK2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22210) · Entrez [222255](https://www.ncbi.nlm.nih.gov/gene/222255) · UniProt [Q9ULK2](https://www.uniprot.org/uniprotkb/Q9ULK2) · Ensembl [ENSG00000146776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146776)

## Data

Gene col 7120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7120); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7120]; `tensor/DDL_lfc|DDL_z.npy` [7120]; `embed/gene_vectors.npy` [7120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7120 or target_col == 7120). Every well: [[ATXN7L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
