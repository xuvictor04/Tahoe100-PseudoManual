---
symbol: "NR4A1"
type: "gene"
col: 4426
ensembl_id: "ENSG00000123358"
name: "nuclear receptor subfamily 4 group A member 1"
location: "12q13.13"
module: 109
arm: "+"
pooled_cpm: 83.18
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 32
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# NR4A1

*nuclear receptor subfamily 4 group A member 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +12.9, q 2e-35, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.365× (z -15.4, q 0e+00, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR4A3]] (+0.72, fdr 7e-06), [[JUNB]] (+0.71, fdr 7e-06), [[HES1]] (+0.71, fdr 7e-06); moves opposite to [[VPS37A]] (-0.63, fdr 1e-05), [[CLCC1]] (-0.59, fdr 1e-05), [[PTPN9]] (-0.57, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SAP30L-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +12.9 | 2e-35 | 28/41 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +9.3 | 4e-18 | 32/42 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +7.1 | 2e-10 | 30/42 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.9 | 7e-10 | 36/42 (SW 900, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +6.9 | 7e-10 | 27/41 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +6.7 | 2e-09 | 29/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 5e-05 | 26/43 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +4.6 | 3e-04 | 25/42 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +4.3 | 0.001 | 26/43 (SK-MEL-2, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.8 | 0.009 | 18/36 (HOP62, RPMI-7951, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.053 | 18/42 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.062 | 16/42 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.365×** | -15.4 | 0e+00 | 38/43 (AsPC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.373×** | -10.2 | 5e-22 | 35/44 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.413×** | -9.5 | 3e-19 | 34/42 (hTERT-HPNE, HT-29, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.424×** | -9.2 | 3e-18 | 33/42 (LS 180, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.415×** | -9.1 | 8e-18 | 34/41 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.586×** | -8.2 | 3e-14 | 32/42 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.477×** | -7.5 | 4e-12 | 33/42 (SW48, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.667×** | -6.2 | 5e-08 | 29/43 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.588×** | -5.7 | 7e-07 | 28/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.603×** | -5.4 | 3e-06 | 31/42 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.610×** | -5.3 | 5e-06 | 28/41 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.599×** | -5.3 | 5e-06 | 26/41 (SHP-77, CFPAC-1, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.599×** | -5.3 | 5e-06 | 27/41 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.663×** | -4.4 | 4e-04 | 21/42 (HT-29, KATO III, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.669×** | -4.2 | 0.001 | 23/41 (SHP-77, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.661×** | -4.1 | 0.001 | 20/42 (SHP-77, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 206 | 11 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -13.0) |
| [[HT-29 (line)]] | alt | 143 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 209 | 1 | 9 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.78× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -12.4) ⚠ toxic; cell-cycle shift, explains <1% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.306× (z -12.0) |
| [[SW48 (line)]] | wt | 449 | 2 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 10.3× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +21.7) | — |
| [[LS 180 (line)]] | wt | 187 | 1 (1 ⚠) | 6 | [[Niclosamide (olamine) (drug)]] 5 µM 3.63× (z +9.0) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 117 | 1 | 6 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0219× (z -24.0) |
| [[hTERT-HPNE (line)]] | wt | 122 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -14.3) |
| [[LoVo (line)]] | wt | 230 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -16.3) |
| [[C-33 A (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -11.7) |
| [[C32 (line)]] | wt | 55.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +20.2) | — |
| [[RPMI-7951 (line)]] | alt | 98.3 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -13.5) |
| [[SHP-77 (line)]] | alt | 168 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -17.1) |
| [[A-427 (line)]] | wt | 104 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 136 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -19.4) |
| [[SW480 (line)]] | alt | 36.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.64× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 29.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 47.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 28.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +14.8) | [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 132 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +16.9) | — |
| [[SW 900 (line)]] | alt | 77.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -8.6) |
| [[SW1417 (line)]] | alt | 111 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -16.1) |
| [[A549 (line)]] | wt | 97.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +12.9) | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -11.0) |
| [[HCT15 (line)]] | alt | 89.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 73.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.1) |
| [[RKO (line)]] | wt | 25.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.33× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +14.4) | — |
| [[A-172 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A3]] | +0.72 | +0.69 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 817 |
| [[JUNB]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 696 |
| [[HES1]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IER2]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 669 |
| [[FOS]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 933 |
| [[NR4A2]] | +0.66 | +0.73 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 782 |
| [[CSRNP1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[EGR2]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 789 |
| [[MIR23AHG]] | +0.64 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PLEKHG2]] | +0.62 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[DUSP2]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 596 |
| [[EGR1]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 873 |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37A]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[CLCC1]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PTPN9]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TMED8]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TRAPPC13]] | -0.56 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[MFSD8]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ZCCHC4]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[URM1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PI4K2B]] | -0.53 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[FAHD2A]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[GPALPP1]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DHX35]] | -0.53 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NR4A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR4A2]] | B | NR4A2 activity raises NR4A1's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 2.23× lower at baseline in the lines without NR4A2 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLITRK6]] | B | SLITRK6 activity raises NR4A1's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without SLITRK6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[EGR2]] | B | EGR2 activity raises NR4A1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without EGR2 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRIM15]] | B | TRIM15 activity raises NR4A1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without TRIM15 | 0.090 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAP30L-AS1]] | B | NR4A1 activity lowers SAP30L-AS1's level | lines that do not express NR4A1 (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without NR4A1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.6, -0.2); signed map (6.5, 27.8). **Vector** length 145, 45.4% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NGF-stimulated transcription* (reactome, mean cos +0.60 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.60 to 9); *Signaling by NTRK1 (TRKA)* (reactome, mean cos +0.60 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.2 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.9 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +12.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.3 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.9 | -7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.7 | -9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.3 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.3 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -9.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 4 group A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,022,832-52,059,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TR3, N10, NAK-1, NGFIB, NUR77; previously HMR, GFRP1 |
| Gene groups (HGNC) | Nuclear receptor subfamily 4 group A |
| Hallmark sets | UV_RESPONSE_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: AKT phosphorylates targets in the nucleus; Constitutive Signaling by AKT1 E17K in Cancer; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P22736](https://www.uniprot.org/uniprotkb/P22736) (Nuclear receptor subfamily 4immunitygroup A member 1):

> Orphan nuclear receptor. Binds the NGFI-B response element (NBRE) 5'-AAAGGTCA-3'. Binds 9-cis-retinoic acid outside of its ligand-binding (NR LBD) domain. Participates in energy homeostasis by sequestrating the kinase STK11 in the nucleus, thereby attenuating cytoplasmic AMPK activation. Regulates the inflammatory response in macrophages by regulating metabolic adaptations during inflammation, including repressing the transcription of genes involved in the citric acid cycle (TCA) (By …

**Summary**, from NCBI Gene [3164](https://www.ncbi.nlm.nih.gov/gene/3164):

> This gene encodes a member of the steroid-thyroid hormone-retinoid receptor superfamily. Expression is induced by phytohemagglutinin in human lymphocytes and by serum stimulation of arrested fibroblasts. The encoded protein acts as a nuclear transcription factor. Translocation of the protein from the nucleus to mitochondria induces apoptosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:7980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7980) · Entrez [3164](https://www.ncbi.nlm.nih.gov/gene/3164) · UniProt [P22736](https://www.uniprot.org/uniprotkb/P22736) · Ensembl [ENSG00000123358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123358)

## Data

Gene col 4426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4426); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4426]; `tensor/DDL_lfc|DDL_z.npy` [4426]; `embed/gene_vectors.npy` [4426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4426 or target_col == 4426). Every well: [[NR4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
