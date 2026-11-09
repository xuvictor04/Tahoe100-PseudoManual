---
symbol: "RIGI"
type: "gene"
col: 2834
ensembl_id: "ENSG00000107201"
name: "RNA sensor RIG-I"
location: "9p21.1"
module: 32
arm: "+"
pooled_cpm: 208.57
n_lines_expressing: 47
n_dd_up: 28
n_dd_down: 64
n_dd_up_clean: 28
n_dd_down_clean: 52
in_vector_space: true
direction_upstream: 39
direction_downstream: 11
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# RIGI

*RNA sensor RIG-I* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 2.73× (z +11.0, q 2e-25, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (12 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.394× (z -14.9, q 0e+00, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT1]] (+0.93, fdr 7e-06), [[IFIH1]] (+0.92, fdr 7e-06), [[OASL]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[OAS3]] → it (grade B ⚠); 11 go from it, the strongest it → [[OASL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, none with an alert; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +11.0 | 2e-25 | 33/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.41×** | +10.0 | 4e-21 | 35/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.8 | 2e-06 | 27/45 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +5.7 | 2e-06 | 25/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +5.3 | 1e-05 | 31/44 (AsPC-1, J82, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.55×** | +4.7 | 2e-04 | 35/46 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.003 | 25/44 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.006 | 21/46 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.007 | 31/45 (NCI-H1792, A498, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.009 | 31/45 (A498, A-172, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.013 | 26/45 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.013 | 22/45 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.026 | 24/46 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.026 | 22/45 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.026 | 24/46 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.394×** | -14.9 | 0e+00 | 35/46 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.406×** | -14.4 | 2e-44 | 38/45 (A549, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.364×** | -11.4 | 8e-28 | 36/46 (A549, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.490×** | -11.4 | 8e-28 | 31/46 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.372×** | -11.2 | 7e-27 | 39/45 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.399×** | -10.4 | 4e-23 | 33/45 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.406×** | -10.2 | 2e-22 | 31/46 (C-33 A, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.411×** | -10.0 | 9e-22 | 40/45 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.417×** | -9.9 | 3e-21 | 40/45 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -9.8 | 8e-21 | 34/41 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.424×** | -9.7 | 2e-20 | 35/46 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.432×** | -9.5 | 2e-19 | 38/45 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.432×** | -8.9 | 2e-17 | 37/45 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.502×** | -7.8 | 3e-13 | 34/45 (NCI-H23, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.503×** | -7.7 | 4e-13 | 35/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.519×** | -7.4 | 5e-12 | 36/45 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.639×** | -7.1 | 4e-11 | 39/46 (NCI-H1573, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 470 | 0 | 25 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.2) |
| [[RKO (line)]] | wt | 274 | 0 | 24 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0769× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 394 | 0 | 18 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.130× (z -18.9) |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 18 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -16.7) |
| [[LoVo (line)]] | wt | 390 | 0 | 17 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.212× (z -16.3) |
| [[SNU-423 (line)]] | alt | 314 | 0 | 17 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.198× (z -14.8) |
| [[A498 (line)]] | wt | 342 | 0 | 13 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.268× (z -15.2) |
| [[A-172 (line)]] | wt | 429 | 1 | 11 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.35× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.235× (z -11.2) |
| [[C-33 A (line)]] | alt | 386 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0637× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 158 | 4 | 8 | [[Harringtonine (drug)]] 5 µM 8.29× (z +16.9) | [[Tofacitinib (drug)]] 5 µM 0.285× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 234 | 2 | 9 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.58× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.180× (z -12.8) |
| [[SHP-77 (line)]] | alt | 156 | 0 | 11 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.122× (z -13.8) |
| [[CHP-212 (line)]] | wt | 262 | 0 | 10 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0631× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.198× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 113 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +32.1) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 197 | 0 | 10 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.303× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 212 | 1 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) | [[Tofacitinib (drug)]] 5 µM 0.262× (z -13.3) |
| [[BT-474 (line)]] | alt | 111 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.253× (z -13.6) |
| [[COLO 205 (line)]] | alt | 449 | 0 | 9 | — | [[Tofacitinib (drug)]] 5 µM 0.123× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 228 | 0 | 9 | — | [[Tofacitinib (drug)]] 5 µM 0.246× (z -12.2) |
| [[HS-578T (line)]] | alt | 292 | 1 | 7 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.43× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.246× (z -13.3) |
| [[KATO III (line)]] | alt | 124 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.272× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 274 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +19.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -11.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 200 | 1 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.64× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 187 | 3 | 3 | [[Harringtonine (drug)]] 5 µM 6.54× (z +13.3) | [[Tofacitinib (drug)]] 5 µM 0.298× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 182 | 0 | 6 | — | [[Selinexor (drug)]] 5 µM 0.293× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 257 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.299× (z -12.1) |
| [[HOP62 (line)]] | alt | 69.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.8) | — |
| [[Hs 766T (line)]] | wt | 355 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 175 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 248 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 4.56× (z +11.3) | [[Tofacitinib (drug)]] 5 µM 0.440× (z -8.9) |
| [[SW48 (line)]] | wt | 65.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 161 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.370× (z -9.4) |
| [[HCT15 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.3) | — |
| [[J82 (line)]] | alt | 180 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.37× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.0) | — |
| [[SNU-1 (line)]] | wt | 132 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.172× (z -8.6) |
| [[A-427 (line)]] | wt | 35.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT1]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 995 |
| [[IFIH1]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 960 |
| [[OASL]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[IFIT3]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 966 |
| [[STAT1]] | +0.91 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 994 |
| [[CMPK2]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 712 |
| [[PARP9]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 830 |
| [[USP18]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 940 |
| [[OAS3]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 943 |
| [[OAS2]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 949 |
| [[MX1]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 971 |
| [[PARP14]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 749 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 28, C 11. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS3]] | B | OAS3 activity raises RIGI's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without OAS3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[RSAD2]] | B | RSAD2 activity raises RIGI's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without RSAD2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[OAS2]] | B | OAS2 activity raises RIGI's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without OAS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[DDX60L]] | B | DDX60L activity raises RIGI's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without DDX60L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises RIGI's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without SAMD9 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[IFI44]] | B | IFI44 activity raises RIGI's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without IFI44 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[ODF3B]] | B | ODF3B activity raises RIGI's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without ODF3B | 0.006 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[CXCL10]] | B | CXCL10 activity weakens RIGI's drug response | lines that do not express CXCL10 (20) vs lines expressing it (26) | the lines without CXCL10 respond 1.35× as strongly (z diff -1.21); strongest at Tofacitinib 0.5 µM: 0.35x vs 0.54x (z diff -2.7) | 0.020 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; target measured in part of the lines |
| [[OASL]] | B | OASL activity raises RIGI's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without OASL | 0.029 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises RIGI's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without MX1 | 0.032 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS1]] | B | OAS1 activity raises RIGI's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without OAS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens RIGI's drug response | lines that do not express IFI6 (11) vs lines expressing it (35) | the lines without IFI6 respond 0.35× as strongly (z diff +2.88); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.78x vs 0.28x (z diff +5.4) | 0.047 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | C | RIGI activity raises OASL's level | lines that do not express RIGI (3) vs lines expressing it (47) | 5.59× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[IFIT2]] | C | RIGI activity raises IFIT2's level | lines that do not express RIGI (3) vs lines expressing it (47) | 5.45× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[DDX60L]] | C | RIGI activity raises DDX60L's level | lines that do not express RIGI (3) vs lines expressing it (47) | 4.79× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[IFIT3]] | C | RIGI activity raises IFIT3's level | lines that do not express RIGI (3) vs lines expressing it (47) | 4.65× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[IFIT1]] | C | RIGI activity raises IFIT1's level | lines that do not express RIGI (3) vs lines expressing it (47) | 4.57× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[IFI44]] | C | RIGI activity raises IFI44's level | lines that do not express RIGI (3) vs lines expressing it (47) | 4.39× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[DDX60]] | C | RIGI activity raises DDX60's level | lines that do not express RIGI (3) vs lines expressing it (47) | 4.35× lower at baseline in the lines without RIGI | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[PARP10]] | C | RIGI's natural level strengthens PARP10's drug response | RIGI's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.66; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMD9]] | C | RIGI activity raises SAMD9's level | lines that do not express RIGI (3) vs lines expressing it (47) | 3.69× lower at baseline in the lines without RIGI | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[ISG15]] | C | RIGI activity raises ISG15's level | lines that do not express RIGI (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without RIGI | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent; its own permutation p |
| [[SP140L]] | C | RIGI activity raises SP140L's level | lines that do not express RIGI (3) vs lines expressing it (47) | 2.60× lower at baseline in the lines without RIGI | 0.0995 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: EXT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.917). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 53.4); signed map (64.6, 31.4). **Vector** length 172, 69.8% of its response variance represented; |z| ≥ 3 in 2,066 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.77 to 56); *Interferon alpha/beta signaling* (reactome, mean cos +0.83 to 27); *Interferon gamma signaling* (reactome, mean cos +0.77 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +13.2 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.3 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +2.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.6 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +1.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.7 | -14.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -11.5 | -14.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.6 | -11.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.0 | -10.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.6 | -10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -8.9 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA sensor RIG-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,455,302-32,526,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIG-I, FLJ13599, DKFZp434J1111, RIG-1, RIG1; previously DDX58 |
| Gene groups (HGNC) | DEAD-box helicases; Caspase recruitment domain containing; RIG-I RNA sensor family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 28 pathways, smallest: OAS antiviral response; NF-kB activation through FADD/RIP-1 pathway mediated by caspase-8 and -10; TRAF3-dependent IRF activation pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O95786](https://www.uniprot.org/uniprotkb/O95786) (Antiviral innate immune response receptor RIG-I):

> Innate immune receptor that senses cytoplasmic viral nucleic acids and activates a downstream signaling cascade leading to the production of type I interferons and pro-inflammatory cytokines. Forms a ribonucleoprotein complex with viral RNAs on which it homooligomerizes to form filaments. The homooligomerization allows the recruitment of RNF135 an E3 ubiquitin-protein ligase that activates and amplifies the RIG-I-mediated antiviral signaling in an RNA length-dependent manner through …

**Summary**, from NCBI Gene [23586](https://www.ncbi.nlm.nih.gov/gene/23586):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases which are implicated in a number of cellular processes involving RNA binding and alteration of RNA secondary structure. This gene encodes a protein containing RNA helicase-DEAD box protein motifs and a caspase recruitment domain (CARD). It is involved in viral double-stranded (ds) RNA recognition and the regulation of the antiviral innate immune response. Mutations in this gene are …

**Accessions** — [HGNC:19102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19102) · Entrez [23586](https://www.ncbi.nlm.nih.gov/gene/23586) · UniProt [O95786](https://www.uniprot.org/uniprotkb/O95786) · Ensembl [ENSG00000107201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107201)

## Data

Gene col 2834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2834); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2834]; `tensor/DDL_lfc|DDL_z.npy` [2834]; `embed/gene_vectors.npy` [2834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2834 or target_col == 2834). Every well: [[RIGI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIGI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
