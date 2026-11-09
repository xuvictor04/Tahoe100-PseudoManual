---
symbol: "PPP4R3B"
type: "gene"
col: 15838
ensembl_id: "ENSG00000275052"
name: "protein phosphatase 4 regulatory subunit 3B"
location: "2p16.1"
module: 83
arm: "+"
pooled_cpm: 172.39
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PPP4R3B

*protein phosphatase 4 regulatory subunit 3B* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.41× (z +10.2, q 2e-21, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.624× (z -13.9, q 6e-41, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H1]] (+0.67, fdr 1e-05), [[RABL3]] (+0.66, fdr 1e-05), [[RBBP6]] (+0.62, fdr 3e-05); moves opposite to [[TRIM35]] (-0.56, fdr 3e-05), [[FAR1]] (-0.55, fdr 4e-05), [[LPCAT4]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +10.2 | 2e-21 | 33/48 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +7.9 | 6e-13 | 24/48 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +6.7 | 5e-09 | 27/48 (NCI-H2030, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +6.0 | 3e-07 | 24/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +5.3 | 1e-05 | 22/48 (HOP62, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 2e-04 | 18/48 (LoVo, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.036 | 14/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.12× | +3.4 | 0.056 | 11/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.13× | +3.1 | 0.11 | 4/50 (A-172, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.11× | +3.0 | 0.13 | 18/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -13.9 | 6e-41 | 43/48 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.640×** | -13.1 | 6e-37 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.649×** | -12.7 | 1e-34 | 38/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -10.5 | 1e-23 | 35/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.740×** | -8.9 | 8e-17 | 36/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -7.8 | 6e-13 | 35/49 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.783×** | -7.2 | 5e-11 | 25/49 (RKO, NCI-H1573, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.801×** | -6.5 | 5e-09 | 29/48 (SW480, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.780×** | -6.2 | 4e-08 | 26/44 (SW48, NCI-H1573, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -4.9 | 5e-05 | 25/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.810×** | -4.3 | 9e-04 | 22/48 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.825×** | -3.9 | 0.004 | 23/48 (SW480, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.910× | -3.9 | 0.004 | 19/49 (A549, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.878× | -3.8 | 0.006 | 14/48 (A549, A-427, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.881× | -3.7 | 0.008 | 13/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.721×** | -3.5 | 0.016 | 16/49 (KATO III, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.895× | -3.3 | 0.034 | 10/48 (LS 180, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 242 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.466× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 216 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.565× (z -10.3) |
| [[A-427 (line)]] | wt | 219 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.502× (z -11.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.595× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 277 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.516× (z -11.1) |
| [[RKO (line)]] | wt | 149 | 3 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.524× (z -8.8) |
| [[SW480 (line)]] | alt | 192 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.532× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 196 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.551× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.600× (z -10.1) |
| [[PANC-1 (line)]] | alt | 173 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.471× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -12.5) |
| [[C32 (line)]] | wt | 159 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.541× (z -8.7) |
| [[HS-578T (line)]] | alt | 112 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.9) | — |
| [[KATO III (line)]] | alt | 206 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -13.2) |
| [[LoVo (line)]] | wt | 144 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 223 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.529× (z -10.3) |
| [[SW 900 (line)]] | alt | 188 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.548× (z -9.6) |
| [[A498 (line)]] | wt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +12.2) | — |
| [[A549 (line)]] | wt | 169 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.475× (z -11.9) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HCT15 (line)]] | alt | 277 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.492× (z -8.8) |
| [[HOP62 (line)]] | alt | 162 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 168 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.502× (z -9.5) |
| [[A-172 (line)]] | wt | 164 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +17.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.428× (z -10.8) |
| [[COLO 205 (line)]] | alt | 225 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.8) | — |
| [[HEC-1-A (line)]] | alt | 157 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.52× (z +9.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[RPMI-7951 (line)]] | alt | 201 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +9.4) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.7) | — |
| [[SNU-1 (line)]] | wt | 186 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.518× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 172 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0750× (z -11.9) |
| [[SW1417 (line)]] | alt | 165 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -9.1) |
| [[SW48 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 163 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 209 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H1]] | +0.67 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RABL3]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[RBBP6]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[CASS4]] | +0.62 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UFC1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LINC01004]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NEK11]] | +0.59 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PCF11]] | +0.59 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[PPWD1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ZNF546]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[THAP2]] | +0.58 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[AKT1S1]] | +0.58 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM35]] | -0.56 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FAR1]] | -0.55 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.54 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[OSTF1]] | -0.54 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[BORCS5]] | -0.54 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[GNA12]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SRPK2]] | -0.53 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[SLC15A4]] | -0.53 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[NUP93]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GPRIN1]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[REPS1]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZFAND4]] | -0.52 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (5.9, 9.5); signed map (20.2, -9.8). **Vector** length 120, 35.7% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.6 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.8 | -10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -5.5 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.3 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,547,292-55,618,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSY2, FLFL2, KIAA1387, FLJ31474; previously SMEK2 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5MIZ7](https://www.uniprot.org/uniprotkb/Q5MIZ7) (Serine/threonine-protein phosphatase 4 regulatory subunit 3B):

> Regulatory subunit of serine/threonine-protein phosphatase 4 (PP4). May regulate the activity of PPP4C at centrosomal microtubule organizing centers.

**Summary**, from NCBI Gene [57223](https://www.ncbi.nlm.nih.gov/gene/57223):

> Predicted to enable protein phosphatase activator activity. Involved in regulation of double-strand break repair. Located in centrosome; chromatin; and nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29267) · Entrez [57223](https://www.ncbi.nlm.nih.gov/gene/57223) · UniProt [Q5MIZ7](https://www.uniprot.org/uniprotkb/Q5MIZ7) · Ensembl [ENSG00000275052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275052)

## Data

Gene col 15838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15838); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15838]; `tensor/DDL_lfc|DDL_z.npy` [15838]; `embed/gene_vectors.npy` [15838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15838 or target_col == 15838). Every well: [[PPP4R3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
