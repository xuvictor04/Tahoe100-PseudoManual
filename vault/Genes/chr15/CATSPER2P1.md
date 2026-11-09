---
symbol: "CATSPER2P1"
type: "gene"
col: 13011
ensembl_id: "ENSG00000205771"
name: "CATSPER2 pseudogene 1"
location: "15q15.3"
module: 15
arm: "+"
pooled_cpm: 10.39
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CATSPER2P1

*CATSPER2 pseudogene 1* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.59× (z +23.3, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.244× (z -15.2, q 0e+00, down in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.448× (z -8.7, q 4e-16, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPER2P1-1]] (+0.85, fdr 7e-06, ⚠ same locus), [[BRPF3-AS1]] (+0.70, fdr 7e-06), [[ZNF213-AS1]] (+0.69, fdr 1e-05), [[CCNO-DT]] (+0.68, fdr 1e-05); moves opposite to [[NAA40]] (-0.53, fdr 7e-04), [[PAFAH1B3]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 16 go from it, the strongest it → [[CATSPER2P1-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.59×** | +23.3 | 0e+00 | 41/42 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +7.8 | 2e-12 | 28/38 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.3 | 2e-05 | 19/40 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 0.002 | 17/43 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 0.003 | 16/45 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.006 | 12/42 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +3.6 | 0.028 | 14/45 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.33× | +3.1 | 0.11 | 8/44 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.11 | 9/44 (A-427, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.244×** | -15.2 | 0e+00 | 38/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.293×** | -13.3 | 1e-37 | 31/39 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.435×** | -12.7 | 1e-34 | 32/42 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.330×** | -11.3 | 2e-27 | 36/43 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.351×** | -10.7 | 1e-24 | 37/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.392×** | -9.7 | 2e-20 | 33/43 (NCI-H460, J82, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.448×** | -8.7 | 4e-16 | 30/43 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.443×** | -8.4 | 2e-15 | 28/33 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.467×** | -8.2 | 2e-14 | 23/44 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.496×** | -7.6 | 2e-12 | 25/41 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.501×** | -7.4 | 7e-12 | 27/42 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.281×** | -7.2 | 4e-11 | 30/38 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.304×** | -6.7 | 8e-10 | 28/43 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.523×** | -6.6 | 2e-09 | 28/42 (LoVo, SW1417, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.380×** | -5.5 | 2e-06 | 17/34 (NCI-H1573, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -4.3 | 6e-04 | 18/41 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.520×** | -3.7 | 0.006 | 12/41 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.045 | 7/44 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.759×** | -2.9 | 0.072 | 9/42 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.593×** | -2.9 | 0.072 | 8/44 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -2.8 | 0.099 | 14/42 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.37 | 1 | 11 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.231× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 52.8 | 1 | 10 (10 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 10.0 | 1 | 8 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +16.3) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.252× (z -9.1) |
| [[LoVo (line)]] | wt | 27.6 | 1 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +15.8) | [[Digitoxin (drug)]] 5 µM 0.0919× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.173× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 40.9 | 1 | 7 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.4) | [[Digitoxin (drug)]] 0.5 µM 0.0880× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 10.3 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0965× (z -12.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +9.7) | [[Harringtonine (drug)]] 0.5 µM 0.126× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 7.78 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0595× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 15.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 13.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.175× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 9.62 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HT-29 (line)]] | alt | 9.51 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 7.76 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +11.1) | [[Fusidic acid (drug)]] 0.5 µM 0.0501× (z -10.6) |
| [[A549 (line)]] | wt | 5.50 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -12.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0190× (z -13.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 7.52 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +10.7) | [[Digitoxin (drug)]] 0.05 µM 0.0394× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 6.33 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0768× (z -9.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 7.79 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0776× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 6.06 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +10.6) | [[Penfluridol (drug)]] 5 µM 0.0502× (z -10.6) |
| [[SW1417 (line)]] | alt | 5.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +10.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0455× (z -11.5) |
| [[A498 (line)]] | wt | 7.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +8.7) | — |
| [[KATO III (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +10.0) | — |
| [[RKO (line)]] | wt | 4.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 8.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +10.1) | — |
| [[SW480 (line)]] | alt | 6.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPER2P1-1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BRPF3-AS1]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CCNO-DT]] | +0.68 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CDNF]] | +0.67 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[DDX59-AS1]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[RNF170]] | +0.65 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FKBP14-AS1]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ING2-DT]] | +0.64 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.64 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RHCE]] | +0.64 | +0.42 / +0.75 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.53 | -0.21 / -0.57 | both halves | 7e-04 |  |
| [[PAFAH1B3]] | -0.52 | -0.29 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CATSPER2P1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers CATSPER2P1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers CATSPER2P1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[CATSPER2P1-1]] | C | CATSPER2P1-1's natural level strengthens CATSPER2P1's drug response | CATSPER2P1-1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.76; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPER2P1-1]] | C | CATSPER2P1's natural level strengthens CATSPER2P1-1's drug response | CATSPER2P1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.71; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[BRPF3-AS1]] | C | CATSPER2P1's natural level strengthens BRPF3-AS1's drug response | CATSPER2P1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.52; direction not clear | 0.028 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CCDC18-AS1]] | C | CATSPER2P1 activity raises CCDC18-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[INHA]] | C | CATSPER2P1 activity raises INHA's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |
| [[PIPOX]] | C | CATSPER2P1 activity raises PIPOX's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |
| [[NIFK-AS1]] | C | CATSPER2P1 activity raises NIFK-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[ATP6V0D1-DT]] | C | CATSPER2P1 activity raises ATP6V0D1-DT's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[RWDD2A]] | C | CATSPER2P1 activity raises RWDD2A's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[SAXO1]] | C | CATSPER2P1 activity raises SAXO1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[DICER1-AS1]] | C | CATSPER2P1 activity raises DICER1-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.65× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |
| [[PNISR-AS1]] | C | CATSPER2P1 activity raises PNISR-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[CRTC3-AS1]] | C | CATSPER2P1 activity raises CRTC3-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.51× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.4, 23.1); signed map (33.4, -4.8). **Vector** length 78.4, 16.9% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +23.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.3 | +3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.5 | +4.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.8 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.7 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -2.8 | -8.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CATSPER2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 15q15.3 — chr15:43,727,181-43,745,165 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | CATSPER2B |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [440278](https://www.ncbi.nlm.nih.gov/gene/440278):

> Catsper genes belong to a family of putative cation channels that are specific to spermatozoa and localize to the flagellum. This gene is part of a tandem repeat on chromosome 15q15; this copy of the gene is thought to be a pseudogene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:31054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31054) · Entrez [440278](https://www.ncbi.nlm.nih.gov/gene/440278) · Ensembl [ENSG00000205771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205771)

## Data

Gene col 13011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13011); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13011]; `tensor/DDL_lfc|DDL_z.npy` [13011]; `embed/gene_vectors.npy` [13011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13011 or target_col == 13011). Every well: [[CATSPER2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPER2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
