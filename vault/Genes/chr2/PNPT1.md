---
symbol: "PNPT1"
type: "gene"
col: 6112
ensembl_id: "ENSG00000138035"
name: "polyribonucleotide nucleotidyltransferase 1"
location: "2p16.1"
module: 32
arm: "+"
pooled_cpm: 111.07
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 36
n_dd_up_clean: 16
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 32
direction_downstream: 36
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PNPT1

*polyribonucleotide nucleotidyltransferase 1* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.73× (z +8.5, q 9e-15, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.452× (z -15.5, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM14]] (+0.92, fdr 7e-06), [[OAS3]] (+0.85, fdr 7e-06), [[SAMHD1]] (+0.85, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[BATF2]] → it (grade B ⚠); 36 go from it, the strongest it → [[TRIM25]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +8.5 | 9e-15 | 32/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +6.4 | 3e-08 | 34/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +6.2 | 1e-07 | 30/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.48×** | +6.1 | 1e-07 | 26/48 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.50×** | +6.1 | 1e-07 | 22/43 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.48×** | +6.1 | 1e-07 | 28/46 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.0 | 2e-07 | 32/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.6 | 2e-06 | 27/47 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 3e-06 | 30/47 (NCI-H2347, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.4 | 3e-06 | 29/47 (RPMI-7951, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +5.4 | 4e-06 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.41×** | +5.0 | 2e-05 | 28/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.77×** | +4.6 | 2e-04 | 31/47 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 2e-04 | 22/47 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.37×** | +4.5 | 2e-04 | 23/44 (J82, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 27/46 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.004 | 23/47 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 23/47 (SK-MEL-2, LS 180, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.011 | 20/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.042 | 16/47 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.051 | 13/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 5 with an alert ⚠; shown: the 15 strongest. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.452×** | -15.5 | 0e+00 | 38/47 (CFPAC-1, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.505×** | -12.8 | 7e-35 | 33/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.476×** | -11.5 | 3e-28 | 36/48 (NCI-H2347, A549, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.505×** | -10.6 | 5e-24 | 36/48 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.559×** | -10.5 | 1e-23 | 32/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.513×** | -10.3 | 4e-23 | 36/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.604×** | -7.8 | 5e-13 | 35/47 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -7.6 | 2e-12 | 29/47 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -7.4 | 7e-12 | 32/48 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.629×** | -7.2 | 4e-11 | 33/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -6.6 | 2e-09 | 31/47 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.463×** | -6.2 | 2e-08 | 32/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.679×** | -6.0 | 1e-07 | 35/48 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.728×** | -4.9 | 4e-05 | 26/47 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.732×** | -4.8 | 6e-05 | 33/47 (BT-474, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 323 | 0 | 15 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 139 | 5 (2 ⚠) | 7 | [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +13.8) | [[Tofacitinib (drug)]] 5 µM 0.287× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 93.1 | 4 (2 ⚠) | 6 | [[Harringtonine (drug)]] 5 µM 4.65× (z +12.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.221× (z -16.1) |
| [[RKO (line)]] | wt | 210 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 176 | 2 | 8 | [[TAK-901 (drug)]] 5 µM 12.5× (z +12.6) | [[Tofacitinib (drug)]] 5 µM 0.314× (z -13.6) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 10 (1 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.182× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 311 | 0 | 9 | — | [[Tofacitinib (drug)]] 0.5 µM 0.284× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 208 | 1 | 7 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.1) | [[Tofacitinib (drug)]] 5 µM 0.251× (z -14.3) |
| [[SW480 (line)]] | alt | 66.5 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.214× (z -16.9) |
| [[C-33 A (line)]] | alt | 263 | 0 | 7 | — | [[Selinexor (drug)]] 5 µM 0.281× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 7 | — | [[Selinexor (drug)]] 5 µM 0.314× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 276 | 0 | 7 | — | [[Selinexor (drug)]] 5 µM 0.240× (z -14.7) |
| [[A-172 (line)]] | wt | 122 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.272× (z -12.3) |
| [[BT-474 (line)]] | alt | 117 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.2) |
| [[HOP62 (line)]] | alt | 31.9 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 123 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.507× (z -11.4) |
| [[A498 (line)]] | wt | 136 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.359× (z -11.2) |
| [[H4 (line)]] | wt | 31.7 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.69× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.308× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 65.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[HS-578T (line)]] | alt | 77.7 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +12.5) | — |
| [[J82 (line)]] | alt | 53.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SHP-77 (line)]] | alt | 200 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.439× (z -11.2) |
| [[C32 (line)]] | wt | 66.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[LoVo (line)]] | wt | 84.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.438× (z -8.8) |
| [[LS 180 (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[Panc 03.27 (line)]] | alt | 78.5 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.346× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.337× (z -11.6) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -8.8) |
| [[A-427 (line)]] | wt | 116 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.505× (z -9.2) |
| [[COLO 205 (line)]] | alt | 125 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.170× (z -12.6) |
| [[HCT15 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[KATO III (line)]] | alt | 95.1 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.257× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 92.8 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.414× (z -8.7) |
| [[AN3 CA (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM14]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS3]] | +0.85 | +0.82 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SAMHD1]] | +0.85 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP9]] | +0.84 | +0.83 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[EIF2AK2]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 507 |
| [[CMPK2]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[STAT1]] | +0.83 | +0.77 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 537 |
| [[MX1]] | +0.83 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PLSCR1]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS2]] | +0.83 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[HERC6]] | +0.80 | +0.76 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 13, C 19. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BATF2]] | B | BATF2 activity raises PNPT1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without BATF2 | 0.026 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises PNPT1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without IFI6 | 0.028 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens PNPT1's drug response | lines that do not express IFI6 (13) vs lines expressing it (35) | the lines without IFI6 respond 0.27× as strongly (z diff +3.11); strongest at Auranofin 5 µM: 0.97x vs 0.51x (z diff +5.6) | 0.033 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BATF2]] | B | BATF2 activity strengthens PNPT1's drug response | lines that do not express BATF2 (12) vs lines expressing it (36) | the lines without BATF2 respond 0.49× as strongly (z diff +2.19); strongest at Auranofin 5 µM: 0.99x vs 0.52x (z diff +5.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS2]] | B | OAS2 activity raises PNPT1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without OAS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP9]] | B | PARP9 activity strengthens PNPT1's drug response | lines that do not express PARP9 (6) vs lines expressing it (42) | the lines without PARP9 respond 0.26× as strongly (z diff +2.75); strongest at Auranofin 5 µM: 1.19x vs 0.55x (z diff +6.5) | 0.043 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS2]] | B | OAS2 activity strengthens PNPT1's drug response | lines that do not express OAS2 (13) vs lines expressing it (35) | the lines without OAS2 respond 0.38× as strongly (z diff +2.28); strongest at Auranofin 5 µM: 0.90x vs 0.53x (z diff +4.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[TRIM22]] | B | TRIM22 activity strengthens PNPT1's drug response | lines that do not express TRIM22 (18) vs lines expressing it (30) | the lines without TRIM22 respond 0.54× as strongly (z diff +1.51); strongest at Auranofin 5 µM: 0.82x vs 0.51x (z diff +4.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1; target measured in part of the lines; artifact flags |
| [[OAS1]] | B | OAS1 activity raises PNPT1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without OAS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises PNPT1's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 1.87× lower at baseline in the lines without PARP9 | 0.086 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity raises PNPT1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[PLSCR1]] | B | PLSCR1 activity strengthens PNPT1's drug response | lines that do not express PLSCR1 (8) vs lines expressing it (40) | the lines without PLSCR1 respond 0.27× as strongly (z diff +2.85); strongest at Auranofin 5 µM: 1.08x vs 0.54x (z diff +6.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 0, C 36. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM25]] | C | PNPT1's natural level strengthens TRIM25's drug response | PNPT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.86, reverse +0.61; direction not clear | 6e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | PNPT1's natural level strengthens IFIT1's drug response | PNPT1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.85, reverse +0.31; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | PNPT1's natural level strengthens HELZ2's drug response | PNPT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.78; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | PNPT1's natural level strengthens USP18's drug response | PNPT1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.85, reverse +0.67; direction not clear | 6e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM14]] | C | PNPT1's natural level strengthens TRIM14's drug response | PNPT1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.76; direction not clear | 9e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | PNPT1's natural level strengthens PARP12's drug response | PNPT1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.63; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | PNPT1's natural level strengthens PML's drug response | PNPT1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.66; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | PNPT1's natural level strengthens TDRD7's drug response | PNPT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.57; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | PNPT1's natural level strengthens ADAR's drug response | PNPT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.67; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | PNPT1's natural level strengthens IRF9's drug response | PNPT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.69; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OAS3]] | C | PNPT1's natural level strengthens OAS3's drug response | PNPT1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.72; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DDX60]] | C | PNPT1's natural level strengthens DDX60's drug response | PNPT1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.29; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 54.8); signed map (65.5, 32.8). **Vector** length 170, 63.4% of its response variance represented; |z| ≥ 3 in 1,703 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.74 to 23); *Interferon Signaling* (reactome, mean cos +0.69 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.72 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.5 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +3.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -14.1 | -15.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -11.1 | -12.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.9 | -10.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.2 | -10.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -10.1 | -11.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -9.2 | -10.6 |

## What is on record

|  |  |
|---|---|
| Name | polyribonucleotide nucleotidyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,634,061-55,693,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNPase, OLD35, old-35; previously DFNB70 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCS8](https://www.uniprot.org/uniprotkb/Q8TCS8) (Polyribonucleotide nucleotidyltransferase 1, mitochondrial):

> RNA-binding protein implicated in numerous RNA metabolic processes. Catalyzes the phosphorolysis of single-stranded polyribonucleotides processively in the 3'-to-5' direction. Mitochondrial intermembrane factor with RNA-processing exoribonulease activity. Component of the mitochondrial degradosome (mtEXO) complex, that degrades 3' overhang double-stranded RNA with a 3'-to-5' directionality in an ATP-dependent manner. Involved in the degradation of non-coding mitochondrial transcripts (MT-ncRNA) …

**Summary**, from NCBI Gene [87178](https://www.ncbi.nlm.nih.gov/gene/87178):

> The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency-13 and autosomal recessive nonsyndromic deafness-70. Related …

**Accessions** — [HGNC:23166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23166) · Entrez [87178](https://www.ncbi.nlm.nih.gov/gene/87178) · UniProt [Q8TCS8](https://www.uniprot.org/uniprotkb/Q8TCS8) · Ensembl [ENSG00000138035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138035)

## Data

Gene col 6112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6112); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6112]; `tensor/DDL_lfc|DDL_z.npy` [6112]; `embed/gene_vectors.npy` [6112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6112 or target_col == 6112). Every well: [[PNPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
