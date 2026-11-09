---
symbol: "TRAF2"
type: "gene"
col: 4794
ensembl_id: "ENSG00000127191"
name: "TNF receptor associated factor 2"
location: "9q34.3"
module: 22
arm: "+"
pooled_cpm: 30.4
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TRAF2

*TNF receptor associated factor 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +20.0, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.632× (z -10.6, q 2e-23, down in 25 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.794× (z -7.5, q 2e-11, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K14]] (+0.56, fdr 1e-05), [[ESPL1]] (+0.56, fdr 1e-05), [[PILRB]] (+0.56, fdr 2e-05); moves opposite to [[GHITM]] (-0.56, fdr 1e-05), [[SDHD]] (-0.55, fdr 1e-05), [[CSDE1]] (-0.52, fdr 2e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +20.0 | 0e+00 | 36/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +12.2 | 9e-32 | 35/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +8.6 | 2e-15 | 26/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +6.1 | 2e-07 | 21/45 (A549, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +5.3 | 2e-05 | 16/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +4.7 | 2e-04 | 13/48 (NCI-H460, BT-474, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +4.5 | 5e-04 | 11/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +4.4 | 8e-04 | 14/48 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 10/48 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 11/44 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.6 | 0.016 | 8/37 (SNU-423, J82, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.6 | 0.016 | 11/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.15× | +3.3 | 0.042 | 6/46 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | 1.15× | +3.2 | 0.049 | 19/47 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +3.2 | 0.054 | 9/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.054 | 8/47 (hTERT-HPNE, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.632×** | -10.6 | 2e-23 | 25/45 (AsPC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -7.5 | 2e-11 | 22/47 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.716×** | -7.1 | 2e-10 | 25/37 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.816×** | -6.6 | 6e-09 | 18/48 (MIA PaCa-2, A498, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -5.7 | 1e-06 | 24/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.779×** | -5.5 | 3e-06 | 18/34 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -5.0 | 5e-05 | 17/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.846× | -3.8 | 0.009 | 9/48 (H4, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.878× | -3.5 | 0.026 | 9/48 (HEC-1-A, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.083 | 10/46 (A498, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.097 | 13/48 (PANC-1, A549, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 64.3 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0973× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.4) |
| [[PANC-1 (line)]] | alt | 42.7 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 22.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.8) | — |
| [[A498 (line)]] | wt | 46.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.3) |
| [[A-172 (line)]] | wt | 49.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -17.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 44.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.7) |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 40.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.0) | [[Docetaxel (drug)]] 0.05 µM 0.327× (z -10.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[J82 (line)]] | alt | 78.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.6) |
| [[LoVo (line)]] | wt | 18.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.20× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.138× (z -8.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K14]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 | pathway: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; STRING 995 |
| [[ESPL1]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PILRB]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SMG9]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TGIF2]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KIF20B]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[DBF4]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MDC1]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[HROB]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[IL4I1]] | +0.51 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SBNO2]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GHITM]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SDHD]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CSDE1]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TMED5]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[VDAC2]] | -0.48 | -0.37 / -0.56 | both halves | 8e-05 | pathway: Deubiquitination |
| [[MTPN]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PGRMC1]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MRPS22]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[SELENOF]] | -0.45 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[EIF3H]] | -0.45 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[LURAP1L]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[CANX]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.8, -52.9); signed map (-51.0, -35.8). **Vector** length 91.7, 18.7% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +20.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +8.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.1 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,881,912-136,926,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP3, RNF117 |
| Gene groups (HGNC) | Ring finger proteins; TNF receptor associated factors; MicroRNA protein coding host genes; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION |
| Reactome | 47 pathways, smallest: Defective RIPK1-mediated regulated necrosis; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12933](https://www.uniprot.org/uniprotkb/Q12933) (TNF receptor-associated factor 2):

> E3 ubiquitin-protein ligase that regulates activation of NF-kappa-B and JNK and plays a central role in the regulation of cell survival and apoptosis. Catalyzes 'Lys-63'-linked ubiquitination of target proteins, such as BIRC3, IKBKE, MLST8, RIPK1 and TICAM1. Is an essential constituent of several E3 ubiquitin-protein ligase complexes, where it promotes the ubiquitination of target proteins by bringing them into contact with other E3 ubiquitin ligases. Regulates BIRC2 and BIRC3 protein levels by …

**Summary**, from NCBI Gene [7186](https://www.ncbi.nlm.nih.gov/gene/7186):

> The protein encoded by this gene is a member of the TNF receptor associated factor (TRAF) protein family. TRAF proteins associate with, and mediate the signal transduction from members of the TNF receptor superfamily. This protein directly interacts with TNF receptors, and forms a heterodimeric complex with TRAF1. This protein is required for TNF-alpha-mediated activation of MAPK8/JNK and NF-kappaB. The protein complex formed by this protein and TRAF1 interacts with the inhibitor-of-apoptosis …

**Accessions** — [HGNC:12032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12032) · Entrez [7186](https://www.ncbi.nlm.nih.gov/gene/7186) · UniProt [Q12933](https://www.uniprot.org/uniprotkb/Q12933) · Ensembl [ENSG00000127191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127191)

## Data

Gene col 4794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4794); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4794]; `tensor/DDL_lfc|DDL_z.npy` [4794]; `embed/gene_vectors.npy` [4794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4794 or target_col == 4794). Every well: [[TRAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
