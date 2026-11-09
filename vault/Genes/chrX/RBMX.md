---
symbol: "RBMX"
type: "gene"
col: 7170
ensembl_id: "ENSG00000147274"
name: "RNA binding motif protein X-linked"
location: "Xq26.3"
module: 85
arm: "-"
pooled_cpm: 151.38
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# RBMX

*RNA binding motif protein X-linked* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.30× (z +14.0, q 8e-42, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +8.7, q 4e-16, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.574× (z -9.3, q 5e-18, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (67 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 33 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.65, fdr 2e-04), [[PBLD]] (+0.64, fdr 8e-04, ⚠ one half only (not replicated)), [[GABPB2]] (+0.64, fdr 9e-05), [[BRD1]] (+0.63, fdr 5e-05); moves opposite to [[YIF1B]] (-0.72, fdr 3e-05), [[MAST3]] (-0.66, fdr 1e-04), [[AP1S1]] (-0.62, fdr 5e-05).
> It sits in the **-** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +14.0 | 8e-42 | 48/49 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.46×** | +9.0 | 6e-17 | 35/48 (AsPC-1, COLO 205, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.7 | 4e-16 | 34/49 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.6 | 2e-15 | 36/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.2 | 4e-14 | 38/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +8.0 | 1e-13 | 42/45 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.55×** | +5.8 | 6e-07 | 37/48 (COLO 205, AsPC-1, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.3 | 9e-06 | 39/50 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 9e-06 | 35/47 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.35×** | +5.0 | 3e-05 | 33/48 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.34×** | +4.9 | 5e-05 | 33/48 (KATO III, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.8 | 9e-05 | 36/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 34/48 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.29×** | +4.4 | 5e-04 | 33/48 (KATO III, AsPC-1, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 33/48 (SW480, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.006 | 24/48 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.044 | 21/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.061 | 16/48 (A-172, HOP62, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.097 | 21/48 (SW480, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -9.3 | 5e-18 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -9.0 | 4e-17 | 45/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -8.9 | 1e-16 | 45/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.722×** | -5.5 | 6e-06 | 34/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -5.2 | 2e-05 | 38/49 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.868× | -3.4 | 0.070 | 12/48 (SW480, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 213 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.478× (z -10.4) |
| [[A498 (line)]] | wt | 105 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 245 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.9) |
| [[HCT15 (line)]] | alt | 183 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.394× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 175 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.8) |
| [[J82 (line)]] | alt | 136 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -10.5) |
| [[KATO III (line)]] | alt | 139 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 184 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 85.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.6) | — |
| [[SW480 (line)]] | alt | 269 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.358× (z -13.0) |
| [[A549 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 94.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +22.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 81.6 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +15.8) ⚠ cell-cycle shift, explains ~60% of this change | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -8.6) |
| [[HOP62 (line)]] | alt | 183 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -10.3) |
| [[LoVo (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 126 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.446× (z -9.3) |
| [[RKO (line)]] | wt | 119 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 145 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.436× (z -9.0) |
| [[SW 900 (line)]] | alt | 103 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.399× (z -8.9) |
| [[A-172 (line)]] | wt | 85.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +13.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 85.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[Hs 766T (line)]] | wt | 97.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 93.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 139 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.407× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 157 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.7) |
| [[SW1417 (line)]] | alt | 151 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[A-427 (line)]] | wt | 233 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H2030 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.7) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H2347 (line)]] | alt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 99.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.5) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[SNU-1 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 176 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 208 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 217 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.65 | +0.57 / +0.30 | both halves | 2e-04 |  |
| [[PBLD]] | +0.64 | +0.60 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[GABPB2]] | +0.64 | +0.62 / +0.36 | both halves | 9e-05 |  |
| [[BRD1]] | +0.63 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[PKN2-AS1]] | +0.63 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[ZBED5]] | +0.63 | +0.63 / +0.26 | both halves | 4e-04 |  |
| [[NQO1-DT]] | +0.62 | +0.59 / +0.25 | both halves | 4e-04 |  |
| [[PCBP1-AS1]] | +0.62 | +0.62 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[RFX3-DT]] | +0.62 | +0.54 / +0.21 | both halves | 7e-04 |  |
| [[EFCAB2]] | +0.62 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.62 | +0.49 / +0.24 | both halves | 5e-04 |  |
| [[HEXIM2-AS1]] | +0.61 | +0.48 / +0.37 | both halves | 7e-05 |  |
| [[MMADHC-DT]] | +0.61 | +0.56 / +0.20 | both halves | 7e-04 |  |
| [[PRDM2]] | +0.61 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.72 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[MAST3]] | -0.66 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[AP1S1]] | -0.62 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[PCMT1]] | -0.62 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[AP2S1]] | -0.60 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[TECPR1]] | -0.58 | -0.43 / -0.23 | both halves | 5e-04 |  |
| [[WRAP73]] | -0.58 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[ST6GALNAC4]] | -0.58 | -0.54 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[FCHO1]] | -0.58 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[STUB1]] | -0.58 | -0.42 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[EHD4]] | -0.57 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[RGS14]] | -0.56 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[GNA12]] | -0.56 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[LRRC42]] | -0.55 | -0.55 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RBMX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.8, 9.7); signed map (23.0, -8.5). **Vector** length 113, 38.1% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +9.5 | +9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +8.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.5 | +0.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.2 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.9 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.2 | -9.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -5.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | +0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:136,848,004-136,880,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNMX, hnRNP-G, HNRNPG |
| Gene groups (HGNC) | RNA binding motif containing; Small nucleolar RNA protein coding host genes; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 18 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P38159](https://www.uniprot.org/uniprotkb/P38159) (RNA-binding motif protein, X chromosome):

> RNA-binding protein that plays several role in the regulation of pre- and post-transcriptional processes. Implicated in tissue-specific regulation of gene transcription and alternative splicing of several pre-mRNAs. Binds to and stimulates transcription from the tumor suppressor TXNIP gene promoter; may thus be involved in tumor suppression. When associated with SAFB, binds to and stimulates transcription from the SREBF1 promoter. Associates with nascent mRNAs transcribed by RNA polymerase II. …

**Summary**, from NCBI Gene [27316](https://www.ncbi.nlm.nih.gov/gene/27316):

> This gene belongs to the RBMY gene family which includes candidate Y chromosome spermatogenesis genes. This gene, an active X chromosome homolog of the Y chromosome RBMY gene, is widely expressed whereas the RBMY gene evolved a male-specific function in spermatogenesis. Pseudogenes of this gene, found on chromosomes 1, 4, 9, 11, and 6, were likely derived by retrotransposition from the original gene. Alternatively spliced transcript variants encoding different isoforms have been identified. A …

**Accessions** — [HGNC:9910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9910) · Entrez [27316](https://www.ncbi.nlm.nih.gov/gene/27316) · UniProt [P38159](https://www.uniprot.org/uniprotkb/P38159) · Ensembl [ENSG00000147274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147274)

## Data

Gene col 7170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7170); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7170]; `tensor/DDL_lfc|DDL_z.npy` [7170]; `embed/gene_vectors.npy` [7170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7170 or target_col == 7170). Every well: [[RBMX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
