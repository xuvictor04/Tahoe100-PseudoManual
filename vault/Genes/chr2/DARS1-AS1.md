---
symbol: "DARS1-AS1"
type: "gene"
col: 13821
ensembl_id: "ENSG00000231890"
name: "DARS1 antisense RNA 1"
location: "2q21.3"
module: 15
arm: "+"
pooled_cpm: 12.66
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DARS1-AS1

*DARS1 antisense RNA 1* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.54× (z +23.8, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.350× (z -16.5, q 0e+00, down in 38 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.227× (z -16.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PELO-AS1]] (+0.80, fdr 7e-06), [[SPESP1]] (+0.76, fdr 7e-06), [[HLA-DMA]] (+0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +23.8 | 0e+00 | 43/43 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +12.2 | 8e-32 | 39/44 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +11.7 | 4e-29 | 37/42 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.2 | 3e-05 | 27/45 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.50×** | +4.4 | 0.001 | 17/44 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.3 | 0.002 | 19/46 (H4, RKO, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.085 | 11/46 (A-172, SW480, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.085 | 18/46 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.32× | +3.1 | 0.12 | 15/45 (A-172, SW 900, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.31× | +3.0 | 0.15 | 10/46 (NCI-H460, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.350×** | -16.5 | 0e+00 | 38/45 (HEC-1-A, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.227×** | -16.5 | 0e+00 | 44/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.257×** | -15.2 | 0e+00 | 45/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -13.3 | 4e-38 | 43/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.355×** | -11.1 | 1e-26 | 30/39 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.383×** | -10.3 | 7e-23 | 37/46 (SW480, HEC-1-A, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.435×** | -9.3 | 1e-18 | 34/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.487×** | -8.0 | 8e-14 | 27/44 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.300×** | -7.0 | 1e-10 | 30/47 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.549×** | -6.7 | 1e-09 | 31/43 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.564×** | -6.4 | 8e-09 | 26/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -6.4 | 8e-09 | 26/43 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.343×** | -6.2 | 2e-08 | 29/43 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -5.5 | 2e-06 | 23/44 (PANC-1, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -5.3 | 4e-06 | 28/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.606×** | -5.3 | 5e-06 | 23/44 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.506×** | -4.0 | 0.002 | 19/46 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.006 | 16/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.748×** | -3.2 | 0.033 | 13/46 (A549, C-33 A, …) | inconsistent across doses |  |
| [[Acetohexamide (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.039 | 16/47 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.5 | 1 | 10 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 32.7 | 1 | 9 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0570× (z -20.0) |
| [[SW480 (line)]] | alt | 24.7 | 2 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.115× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.131× (z -12.9) |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0711× (z -13.9) |
| [[KATO III (line)]] | alt | 14.6 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.0957× (z -12.7) |
| [[COLO 205 (line)]] | alt | 15.6 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.124× (z -9.9) |
| [[HT-29 (line)]] | alt | 15.7 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.0615× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 17.9 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -11.2) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.180× (z -10.0) |
| [[LoVo (line)]] | wt | 17.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +16.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -11.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -8.9) |
| [[LS 180 (line)]] | wt | 9.53 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.104× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +15.0) | [[Harringtonine (drug)]] 5 µM 0.117× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.162× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.181× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.114× (z -9.6) |
| [[PANC-1 (line)]] | alt | 8.35 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +17.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HepG2_C3A (line)]] | wt | 13.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.117× (z -8.6) |
| [[HOP62 (line)]] | alt | 16.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 14.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0831× (z -11.7) ⚠ toxic |
| [[RKO (line)]] | wt | 6.78 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.0960× (z -8.5) |
| [[A-172 (line)]] | wt | 8.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +10.8) | — |
| [[A549 (line)]] | wt | 6.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 7.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +12.9) | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 8.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 8.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -9.2) |
| [[SW 900 (line)]] | alt | 9.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 6.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +12.4) | — |
| [[A-427 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELO-AS1]] | +0.80 | +0.71 / +0.66 | both halves | 7e-06 | same gene group |
| [[SPESP1]] | +0.76 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HLA-DMA]] | +0.74 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.74 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[ANKRD17-DT]] | +0.74 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CASS4]] | +0.73 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | +0.73 | +0.62 / +0.68 | both halves | 7e-06 | same gene group |
| [[NIFK-AS1]] | +0.73 | +0.64 / +0.63 | both halves | 7e-06 | same gene group |
| [[INTS6-AS1]] | +0.73 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[PHC2-AS1]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 | same gene group |
| [[RNF217-AS1]] | +0.71 | +0.48 / +0.59 | both halves | 2e-05 | same gene group |
| [[CHD1-DT]] | +0.70 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DARS1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01762]] | B | LINC01762 activity raises DARS1-AS1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without LINC01762 | 0.018 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[DDX59-AS1]] | B | DDX59-AS1 activity raises DARS1-AS1's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without DDX59-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[ZSWIM5]] | B | ZSWIM5 activity raises DARS1-AS1's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 2.05× lower at baseline in the lines without ZSWIM5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |
| [[RAPGEF4]] | B | RAPGEF4 activity raises DARS1-AS1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without RAPGEF4 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers DARS1-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RFX3-DT]] | C | RFX3-DT activity raises DARS1-AS1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[C4orf47]] | C | C4orf47 activity raises DARS1-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without C4orf47 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | DARS1-AS1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | DARS1-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.390 over the table, 0.041 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.5, 21.0); signed map (27.3, -6.1). **Vector** length 110, 29.6% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.4 | +23.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.6 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.2 | -13.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -15.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -16.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DARS1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q21.3 — chr2:135,985,124-136,022,593 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously DARS-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40170) · Entrez [101928243](https://www.ncbi.nlm.nih.gov/gene/101928243) · Ensembl [ENSG00000231890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231890)

## Data

Gene col 13821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13821); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13821]; `tensor/DDL_lfc|DDL_z.npy` [13821]; `embed/gene_vectors.npy` [13821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13821 or target_col == 13821). Every well: [[DARS1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DARS1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
