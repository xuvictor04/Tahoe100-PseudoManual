---
symbol: "RUSC2"
type: "gene"
col: 12708
ensembl_id: "ENSG00000198853"
name: "RUN and SH3 domain containing 2"
location: "9p13.3"
module: 18
arm: "+"
pooled_cpm: 73.59
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RUSC2

*RUN and SH3 domain containing 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.37× (z +7.7, q 9e-12, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.532× (z -15.4, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF9]] (+0.66, fdr 7e-06), [[C19orf12]] (+0.64, fdr 9e-06), [[SNX24]] (+0.63, fdr 1e-05); moves opposite to [[REL]] (-0.57, fdr 1e-05), [[HMGN2]] (-0.53, fdr 2e-05), [[CNOT1]] (-0.53, fdr 7e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 9 go from it, the strongest it → [[UBE2Q2P1-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +7.7 | 9e-12 | 29/45 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 2e-11 | 33/44 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +6.9 | 1e-09 | 31/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 1e-05 | 26/44 (SW480, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 6e-05 | 29/44 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +4.9 | 9e-05 | 22/43 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.7 | 2e-04 | 22/44 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.9 | 0.007 | 13/44 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +3.5 | 0.026 | 18/44 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.026 | 18/44 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.035 | 14/44 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.049 | 16/44 (A-427, RKO, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.051 | 15/43 (AsPC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.063 | 8/45 (KATO III, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -15.4 | 0e+00 | 39/45 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.412×** | -15.3 | 0e+00 | 43/44 (HS-578T, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -14.6 | 1e-45 | 34/44 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.453×** | -13.7 | 2e-40 | 42/44 (HS-578T, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.445×** | -13.4 | 4e-39 | 38/46 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.468×** | -12.6 | 2e-34 | 34/44 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.482×** | -12.1 | 6e-32 | 27/38 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -12.0 | 3e-31 | 38/44 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.551×** | -10.3 | 5e-23 | 33/45 (SNU-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.603×** | -8.1 | 4e-14 | 28/41 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.627×** | -8.0 | 5e-14 | 32/44 (A-172, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -6.2 | 3e-08 | 26/44 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -6.0 | 8e-08 | 27/44 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.715×** | -5.8 | 3e-07 | 26/44 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.7 | 4e-07 | 22/44 (A-172, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.6 | 1e-04 | 21/44 (A-172, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -4.1 | 0.001 | 23/44 (LoVo, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.013 | 14/44 (SW 1271, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.034 | 15/44 (NCI-H23, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 102 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -26.6) |
| [[HS-578T (line)]] | alt | 104 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -22.6) |
| [[J82 (line)]] | alt | 173 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -20.1) |
| [[A498 (line)]] | wt | 142 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 53.4 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 8 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -15.1) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -15.0) |
| [[PANC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.94× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.318× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.324× (z -11.3) |
| [[RKO (line)]] | wt | 168 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 147 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.37× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.2) |
| [[H4 (line)]] | wt | 110 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -13.1) |
| [[SNU-423 (line)]] | alt | 84.3 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.6) |
| [[A549 (line)]] | wt | 135 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -20.5) |
| [[HOP62 (line)]] | alt | 70.4 | 0 | 4 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.214× (z -13.7) ⚠ transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.305× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 97.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 74.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -11.2) |
| [[Hs 766T (line)]] | wt | 97.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 63.9 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.26× (z +8.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.8) |
| [[SW480 (line)]] | alt | 29.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 43.4 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.25× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -16.1) |
| [[SNU-1 (line)]] | wt | 247 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0342× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.0) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.6) |
| [[A-427 (line)]] | wt | 57.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.251× (z -8.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.4) |
| [[C32 (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.4) |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0879× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SK-MEL-2 (line)]] | alt | 50.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.0) |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0937× (z -10.2) |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF9]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[C19orf12]] | +0.64 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[SNX24]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[GSTO1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SMAGP]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NBPF15]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[NBPF20]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MPP3]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 | same gene group |
| [[SLC22A15]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SIMC1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.58 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[DAP3]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REL]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.53 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[CNOT1]] | -0.53 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[BCL3]] | -0.53 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ARL5B]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PER2]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TAPBP]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GPD2]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[EFNA1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[DNAH7]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[C4orf33]] | -0.50 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises RUSC2's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without HEG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[TOP2A]] | B | TOP2A activity raises RUSC2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P1-1]] | C | RUSC2 activity raises UBE2Q2P1-1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without RUSC2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[ITGB1BP1]] | C | RUSC2 activity raises ITGB1BP1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without RUSC2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[LIMK1]] | C | RUSC2 activity raises LIMK1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without RUSC2 | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |
| [[RNF216]] | C | RUSC2 activity raises RNF216's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without RUSC2 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |
| [[RGS10]] | C | RUSC2 activity raises RGS10's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[PER2]] | C | RUSC2 activity lowers PER2's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[ZFYVE9]] | C | RUSC2 activity raises ZFYVE9's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[MPP3]] | C | RUSC2 activity raises MPP3's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without RUSC2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |
| [[GID4]] | C | RUSC2 activity raises GID4's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without RUSC2 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (20.8, -24.9); signed map (-17.5, 46.8). **Vector** length 113, 33.7% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.3 | +7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.3 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.5 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +5.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -12.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RUN and SH3 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,490,111-35,561,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0375 |
| Gene groups (HGNC) | RUN domain containing; RUN and SH3 domain containing family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2Y8](https://www.uniprot.org/uniprotkb/Q8N2Y8) (AP-4 complex accessory subunit RUSC2):

> Associates with the adapter-like complex 4 (AP-4) and may therefore play a role in vesicular trafficking of proteins at the trans-Golgi network.

**Summary**, from NCBI Gene [9853](https://www.ncbi.nlm.nih.gov/gene/9853):

> This gene encodes a RUN and SH3 domain containing protein that interacts with Rab1b and Rab1-binding protein GM130. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:23625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23625) · Entrez [9853](https://www.ncbi.nlm.nih.gov/gene/9853) · UniProt [Q8N2Y8](https://www.uniprot.org/uniprotkb/Q8N2Y8) · Ensembl [ENSG00000198853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198853)

## Data

Gene col 12708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12708); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12708]; `tensor/DDL_lfc|DDL_z.npy` [12708]; `embed/gene_vectors.npy` [12708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12708 or target_col == 12708). Every well: [[RUSC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUSC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
