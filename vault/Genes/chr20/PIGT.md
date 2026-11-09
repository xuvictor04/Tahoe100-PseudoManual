---
symbol: "PIGT"
type: "gene"
col: 4487
ensembl_id: "ENSG00000124155"
name: "phosphatidylinositol glycan anchor biosynthesis class T"
location: "20q13.12"
module: 50
arm: "+"
pooled_cpm: 41.52
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PIGT

*phosphatidylinositol glycan anchor biosynthesis class T* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +18.8, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +7.8, q 1e-12, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.689× (z -6.1, q 7e-07, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMP1]] (+0.80, fdr 7e-06), [[EMC1]] (+0.77, fdr 7e-06), [[NCSTN]] (+0.72, fdr 7e-06); moves opposite to [[NSUN5P2-1]] (-0.61, fdr 4e-05, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[PDCD5]] (-0.60, fdr 3e-05), [[EIF5B]] (-0.58, fdr 1e-04), [[UBE2B]] (-0.56, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +18.8 | 0e+00 | 45/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +15.5 | 0e+00 | 37/37 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +12.9 | 8e-36 | 39/43 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.8 | 1e-12 | 34/47 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.5 | 7e-09 | 35/46 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +4.9 | 7e-05 | 25/48 (A-172, SW480, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.9 | 7e-05 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.32×** | +4.7 | 2e-04 | 27/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.4 | 7e-04 | 24/49 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.27×** | +3.9 | 0.006 | 20/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.22×** | +3.4 | 0.032 | 18/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.033 | 16/35 (HS-578T, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.21×** | +3.2 | 0.054 | 16/48 (COLO 205, NCI-H460, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.2 | 0.058 | 15/48 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.063 | 11/48 (HS-578T, NCI-H661, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.689×** | -6.1 | 7e-07 | 31/48 (HS-578T, SW 1088, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 2e-04 | 25/48 (LS 180, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.796×** | -3.7 | 0.037 | 16/47 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.860× | -3.6 | 0.039 | 12/48 (Hs 766T, SW480, …) | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | 0.873× | -3.3 | 0.099 | 14/48 (SHP-77, LS 180, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.099 | 13/48 (J82, SW 1271, …) | two highest doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.875× | -3.2 | 0.100 | 14/48 (RKO, HT-29, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.11 | 8/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.15 | 13/47 (H4, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 35.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 44.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 32.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +10.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 58.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 56.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 45.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +14.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 78.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.7) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 42.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.66× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.247× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 75.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0802× (z -9.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP1]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[EMC1]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[GNS]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SF3B4]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[BAG6]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PPP2R1A]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[CDK16]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[BSG]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[GPAA1]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 | same gene group; pathway: Attachment of GPI anchor to uPAR; STRING 999 |

## Genes that move opposite

*15 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P2-1]] ⚠ | -0.61 | -0.41 / -0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDCD5]] | -0.60 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.58 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.58 | -0.37 / -0.65 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOL7]] ⚠ | -0.57 | -0.30 / -0.63 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | -0.57 | -0.31 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PPP1R35]] ⚠ | -0.56 | -0.32 / -0.58 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2B]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[NSUN5P1-1]] | -0.55 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CROCCP2-1]] | -0.55 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[MED10]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SNHG6]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SNHG7]] | -0.54 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[MRPS18C]] | -0.53 | -0.22 / -0.63 | both halves | 6e-04 |  |
| [[SNHG8]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIGT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHRDL1]] | B | CHRDL1 activity raises PIGT's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.43× lower at baseline in the lines without CHRDL1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[POGLUT3]] | B | POGLUT3 activity raises PIGT's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without POGLUT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -22.4); signed map (-22.4, -36.9). **Vector** length 82.2, 17.3% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +18.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,416,084-45,456,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-T |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; MicroRNA protein coding host genes; Glycosylphosphatidylinositol transamidase complex |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969N2](https://www.uniprot.org/uniprotkb/Q969N2) (GPI-anchor transamidase component PIGT):

> Component of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis. May play a crucial role in GPI-T complex assembly in the luminal layer. Binds GPI-anchor.

**Summary**, from NCBI Gene [51604](https://www.ncbi.nlm.nih.gov/gene/51604):

> This gene encodes a protein that is involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This protein is an essential component of the multisubunit enzyme, GPI transamidase. GPI transamidase mediates GPI anchoring in the endoplasmic reticulum, by catalyzing the transfer of fully assembled GPI units to proteins. Alternatively spliced transcript variants encoding multiple …

**Accessions** — [HGNC:14938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14938) · Entrez [51604](https://www.ncbi.nlm.nih.gov/gene/51604) · UniProt [Q969N2](https://www.uniprot.org/uniprotkb/Q969N2) · Ensembl [ENSG00000124155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124155)

## Data

Gene col 4487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4487); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4487]; `tensor/DDL_lfc|DDL_z.npy` [4487]; `embed/gene_vectors.npy` [4487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4487 or target_col == 4487). Every well: [[PIGT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
