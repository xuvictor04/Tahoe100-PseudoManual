---
symbol: "SAMD9"
type: "gene"
col: 12976
ensembl_id: "ENSG00000205413"
name: "sterile alpha motif domain containing 9"
location: "7q21.2"
module: 32
arm: "+"
pooled_cpm: 89.3
n_lines_expressing: 39
n_dd_up: 48
n_dd_down: 41
n_dd_up_clean: 47
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 57
direction_downstream: 83
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SAMD9

*sterile alpha motif domain containing 9* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 5.05× (z +13.3, q 8e-38, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.397× (z -10.7, q 5e-24, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD9L]] (+0.91, fdr 7e-06, ⚠ same locus), [[DDX60L]] (+0.89, fdr 7e-06), [[PARP14]] (+0.89, fdr 7e-06), [[IFIT3]] (+0.89, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 83 go from it, the strongest it → [[SP100]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 1 with an alert ⚠; shown: the 15 strongest. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **5.05×** | +13.3 | 8e-38 | 37/37 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +9.2 | 1e-17 | 31/37 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.42×** | +7.0 | 4e-10 | 34/36 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.33×** | +7.0 | 4e-10 | 30/37 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.16×** | +6.4 | 2e-08 | 34/37 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +5.4 | 8e-06 | 24/37 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.90×** | +5.3 | 1e-05 | 34/37 (NCI-H1792, A-172, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.93×** | +5.0 | 4e-05 | 26/36 (NCI-H460, C32, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.84×** | +4.8 | 8e-05 | 29/37 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.78×** | +4.7 | 1e-04 | 33/36 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 26/37 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 7e-04 | 26/37 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.68×** | +4.3 | 8e-04 | 28/37 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 25/38 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.002 | 27/38 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.397×** | -10.7 | 5e-24 | 29/38 (LoVo, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.469×** | -8.8 | 5e-16 | 29/38 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.387×** | -7.8 | 1e-12 | 30/37 (SHP-77, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.395×** | -7.6 | 3e-12 | 29/37 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.410×** | -7.3 | 3e-11 | 35/37 (NCI-H460, RKO, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -7.0 | 3e-10 | 32/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.456×** | -6.4 | 9e-09 | 30/38 (KATO III, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.470×** | -6.2 | 4e-08 | 31/38 (A-172, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -5.7 | 7e-07 | 27/37 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -5.6 | 9e-07 | 28/37 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -5.3 | 6e-06 | 29/37 (SNU-423, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -5.1 | 1e-05 | 27/37 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -5.0 | 3e-05 | 30/36 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -4.9 | 3e-05 | 23/37 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -4.6 | 2e-04 | 25/37 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.585×** | -4.4 | 4e-04 | 30/37 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.594×** | -4.3 | 6e-04 | 27/37 (LoVo, BT-474, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.601×** | -4.2 | 9e-04 | 20/36 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 76.1 | 0 | 11 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.193× (z -12.6) |
| [[RKO (line)]] | wt | 99.8 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -22.0) |
| [[A-172 (line)]] | wt | 425 | 0 | 10 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -13.0) ⚠ toxic · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.127× (z -12.1) |
| [[LoVo (line)]] | wt | 95.5 | 2 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.10× (z +10.7) | [[Tofacitinib (drug)]] 5 µM 0.196× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 206 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.0) | [[Tofacitinib (drug)]] 5 µM 0.340× (z -10.4) |
| [[COLO 205 (line)]] | alt | 203 | 2 | 5 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.01× (z +11.9) | [[Tofacitinib (drug)]] 5 µM 0.267× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 5 | 2 | [[Harringtonine (drug)]] 0.5 µM 15.6× (z +15.8) | [[Tofacitinib (drug)]] 5 µM 0.226× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 242 | 1 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.18× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.194× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 228 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 8.01× (z +13.0) | [[Tofacitinib (drug)]] 5 µM 0.278× (z -11.8) |
| [[KATO III (line)]] | alt | 104 | 1 | 5 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 12.7× (z +13.9) | [[Tofacitinib (drug)]] 5 µM 0.254× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 279 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.6) |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 45.4 | 4 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.48× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -14.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 58.6 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 11.3× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 179 | 3 | 1 | [[Harringtonine (drug)]] 0.5 µM 7.62× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.175× (z -9.3) |
| [[J82 (line)]] | alt | 91.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.79× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.85× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0880× (z -10.9) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.223× (z -9.9) |
| [[A498 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.271× (z -10.1) |
| [[HT-29 (line)]] | alt | 47.5 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.42× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -9.0) |
| [[PANC-1 (line)]] | alt | 24.2 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.93× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.6) |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.181× (z -10.6) |
| [[H4 (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -8.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.76× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 93.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.197× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 116 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 11.4× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.57× (z +9.8) | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0630× (z -8.6) |
| [[SW 1271 (line)]] | alt | 67.6 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0665× (z -8.7) |
| [[SW 900 (line)]] | alt | 70.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.14× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 54.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.56× (z +10.6) | — |
| [[A-427 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 392 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD9L]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 794; ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[DDX60L]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | STRING 815 |
| [[PARP14]] | +0.89 | +0.85 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 556 |
| [[IFIT3]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 779 |
| [[RSAD2]] | +0.89 | +0.84 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 858 |
| [[DDX60]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 893 |
| [[XAF1]] | +0.88 | +0.81 / +0.89 | both halves | 7e-06 | STRING 737 |
| [[IFIT1]] | +0.87 | +0.81 / +0.89 | both halves | 7e-06 | STRING 724 |
| [[OAS2]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | STRING 848 |
| [[IFIT2]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 781 |
| [[IFIT5]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 665 |
| [[PARP9]] | +0.86 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 804 |
| [[HERC6]] | +0.86 | +0.80 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 740 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 49, C 8. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises SAMD9's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 4.29× lower at baseline in the lines without SAMD9L | 8e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[RSAD2]] | B | RSAD2 activity raises SAMD9's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TRIM22]] | B | TRIM22 activity raises SAMD9's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.73× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFI16]] | B | IFI16 activity raises SAMD9's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 4.13× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[OAS2]] | B | OAS2 activity raises SAMD9's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.97× lower at baseline in the lines without OAS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[NLRC5]] | B | NLRC5 activity raises SAMD9's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.80× lower at baseline in the lines without NLRC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises SAMD9's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.13× lower at baseline in the lines without CTSS | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises SAMD9's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[APOL1]] | B | APOL1 activity raises SAMD9's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 3.38× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[OAS1]] | B | OAS1 activity raises SAMD9's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without OAS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises SAMD9's level | lines that do not express CD5L (23) vs lines expressing it (27) | 3.82× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[MMP13]] | B | MMP13 activity raises SAMD9's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without MMP13 | 0.007 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |

### Downstream of this gene

*83 arrows, 83 of them with an alert ⚠; grade A 0, B 77, C 6. Shown: the 12 strongest; 71 more arrows (71 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SP100]] | B | SAMD9 activity raises SP100's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without SAMD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[PLSCR1]] | B | SAMD9 activity raises PLSCR1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without SAMD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[PARP14]] | B | SAMD9 activity raises PARP14's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without SAMD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS2]] | B | SAMD9 activity raises OAS2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 4.69× lower at baseline in the lines without SAMD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[HERC6]] | B | SAMD9 activity raises HERC6's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without SAMD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RIGI]] | B | SAMD9 activity raises RIGI's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without SAMD9 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[SP110]] | B | SAMD9 activity raises SP110's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without SAMD9 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[NLRC5]] | B | SAMD9 activity raises NLRC5's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without SAMD9 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS3]] | B | SAMD9 activity raises OAS3's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.52× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[PARP9]] | B | SAMD9 activity raises PARP9's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.40× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RSAD2]] | B | SAMD9 activity raises RSAD2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.60× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[DDX60L]] | B | SAMD9 activity raises DDX60L's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.87× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.896). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 54.1); signed map (63.6, 32.2). **Vector** length 168, 65.8% of its response variance represented; |z| ≥ 3 in 1,632 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.75 to 60); *interferon* (control, mean cos +0.83 to 23); *Interferon Signaling* (reactome, mean cos +0.76 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +14.1 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.7 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.1 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.7 | +7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.8 | +4.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.3 | -10.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.9 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.5 | -7.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.5 | -6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.1 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:93,099,513-93,118,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2004, FLJ20073; previously C7orf5 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5K651](https://www.uniprot.org/uniprotkb/Q5K651) (Sterile alpha motif domain-containing protein 9):

> Double-stranded nucleic acid binding that acts as an antiviral factor by playing an essential role in the formation of cytoplasmic antiviral granules. May play a role in the inflammatory response to tissue injury and the control of extra-osseous calcification, acting as a downstream target of TNF signaling. Involved in the regulation of EGR1, in coordination with RGL2. May be involved in endosome fusion.

**Summary**, from NCBI Gene [54809](https://www.ncbi.nlm.nih.gov/gene/54809):

> This gene encodes a sterile alpha motif domain-containing protein. The encoded protein localizes to the cytoplasm and may play a role in regulating cell proliferation and apoptosis. Mutations in this gene are the cause of normophosphatemic familial tumoral calcinosis. Alternate splicing results in multiple transcript variants that encode the same protein.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:1348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1348) · Entrez [54809](https://www.ncbi.nlm.nih.gov/gene/54809) · UniProt [Q5K651](https://www.uniprot.org/uniprotkb/Q5K651) · Ensembl [ENSG00000205413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205413)

## Data

Gene col 12976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12976); `tables/drug_effects.parquet` (89 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12976]; `tensor/DDL_lfc|DDL_z.npy` [12976]; `embed/gene_vectors.npy` [12976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12976 or target_col == 12976). Every well: [[SAMD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
