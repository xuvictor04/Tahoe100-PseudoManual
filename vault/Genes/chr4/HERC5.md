---
symbol: "HERC5"
type: "gene"
col: 6203
ensembl_id: "ENSG00000138646"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase 5"
location: "4q22.1"
module: 32
arm: "+"
pooled_cpm: 51.73
n_lines_expressing: 35
n_dd_up: 16
n_dd_down: 66
n_dd_up_clean: 14
n_dd_down_clean: 55
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# HERC5

*HECT and RLD domain containing E3 ubiquitin protein ligase 5* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.74× (z +6.7, q 9e-09, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 66 drug-doses (11 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.389× (z -11.9, q 7e-30, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT1]] (+0.89, fdr 7e-06), [[OASL]] (+0.89, fdr 7e-06), [[OAS1]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[OASL]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NT5C3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +6.7 | 9e-09 | 17/33 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[venetoclax (drug)]] 0.05 µM |  | **1.63×** | +5.9 | 1e-06 | 23/33 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.8 | 1e-06 | 18/33 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +5.5 | 4e-06 | 18/32 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.35×** | +5.4 | 7e-06 | 16/33 (NCI-H2030, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +4.3 | 0.002 | 16/33 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.002 | 14/33 (CFPAC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.018 | 13/33 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.025 | 12/33 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.030 | 7/33 (A498, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.030 | 13/33 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.036 | 12/32 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.037 | 12/33 (A498, A549, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.051 | 13/33 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.056 | 7/33 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.066 | 9/33 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 71 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 66 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.389×** | -11.9 | 7e-30 | 23/33 (A549, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.513×** | -11.8 | 7e-30 | 30/33 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.396×** | -11.6 | 5e-29 | 20/33 (NCI-H2347, CHP-212, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.531×** | -11.2 | 4e-27 | 22/33 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.425×** | -10.8 | 6e-25 | 26/33 (CFPAC-1, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.427×** | -10.7 | 1e-24 | 28/33 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.456×** | -9.9 | 5e-21 | 25/33 (A-172, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -9.8 | 5e-21 | 19/31 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.485×** | -9.1 | 6e-18 | 27/33 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.613×** | -8.7 | 2e-16 | 20/33 (NCI-H2347, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.508×** | -8.5 | 1e-15 | 21/33 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.512×** | -8.1 | 3e-14 | 21/31 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.552×** | -7.5 | 4e-12 | 26/32 (A-172, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.542×** | -7.4 | 7e-12 | 23/32 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.569×** | -7.1 | 6e-11 | 19/31 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.680×** | -6.8 | 3e-10 | 20/33 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.589×** | -6.6 | 1e-09 | 20/33 (SNU-423, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.374×** | -6.5 | 3e-09 | 18/32 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.606×** | -6.3 | 1e-08 | 23/32 (A-172, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.498×** | -6.2 | 1e-08 | 20/33 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.393×** | -6.1 | 2e-08 | 20/33 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 97.1 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -20.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0561× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 228 | 2 | 13 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.76× (z +9.7) | [[Tofacitinib (drug)]] 5 µM 0.176× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 110 | 13 (9 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +21.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.30× (z +16.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -14.4) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 144 | 0 | 11 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.336× (z -13.4) |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 10 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.154× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 10 (2 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0859× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 93.9 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.164× (z -17.5) |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 9 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.216× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 96.8 | 0 | 8 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.172× (z -15.9) |
| [[A-172 (line)]] | wt | 125 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.388× (z -9.8) |
| [[C-33 A (line)]] | alt | 59.2 | 0 | 7 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -11.7) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.0957× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 86.2 | 0 | 7 (2 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.157× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.182× (z -11.4) |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.0552× (z -15.4) |
| [[J82 (line)]] | alt | 39.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.23× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 55.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +16.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1792 (line)]] | alt | 57.9 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.209× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 47.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +23.7) ⚠ cell-cycle shift, explains ~50% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -9.0) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +11.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.270× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -15.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0746× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.441× (z -8.9) |
| [[A-427 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT1]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 963 |
| [[OASL]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 947 |
| [[OAS1]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 850 |
| [[IFIT3]] | +0.87 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 939 |
| [[TRANK1]] | +0.86 | +0.85 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[IFI44]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 914 |
| [[IFIH1]] | +0.86 | +0.82 / +0.90 | both halves | 7e-06 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta; STRING 925 |
| [[RIGI]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 960 |
| [[STAT1]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 807 |
| [[IFIT2]] | +0.85 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 937 |
| [[CMPK2]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | STRING 698 |
| [[OAS2]] | +0.85 | +0.79 / +0.86 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 902 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | OASL activity raises HERC5's level | lines that do not express OASL (10) vs lines expressing it (40) | 4.74× lower at baseline in the lines without OASL | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers HERC5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TRIM34]] | B | TRIM34 activity raises HERC5's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 4.11× lower at baseline in the lines without TRIM34 | 0.084 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity strengthens HERC5's drug response | lines that do not express OAS1 (9) vs lines expressing it (24) | the lines without OAS1 respond 0.31× as strongly (z diff +2.90); strongest at Dinaciclib 5 µM: 1.27x vs 0.47x (z diff +5.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises HERC5's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without MX1 | 0.098 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5C3A]] | B | HERC5 activity lowers NT5C3A's level | lines that do not express HERC5 (15) vs lines expressing it (35) | 1.51× higher at baseline in the lines without HERC5 | 0.085 | ⚠ within organs, on part of the lines; also absent: RAB31, CACNG6, MYOSLID |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.878). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 53.1); signed map (64.9, 30.9). **Vector** length 147, 46.9% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.74 to 56); *interferon gamma response* (hallmark, mean cos +0.75 to 60); *Interferon alpha/beta signaling* (reactome, mean cos +0.80 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.9 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.0 | +5.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.0 | -11.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.1 | -11.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -8.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.8 | -6.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.2 | -11.6 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,457,119-88,506,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEB1 |
| Gene groups (HGNC) | HECT and RLD domain containing E3 ubiquitin protein ligases |
| Reactome | 15 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Negative regulators of DDX58/IFIH1 signaling; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UII4](https://www.uniprot.org/uniprotkb/Q9UII4) (E3 ISG15--protein ligase HERC5):

> Major E3 ligase for ISG15 conjugation. Functions as part of the ISGylation machinery that recognizes target proteins in a broad and relatively non-specific manner. Physically associated with polyribosomes, broadly modifies newly synthesized proteins in a cotranslational manner. Acts as a positive regulator of innate antiviral response in cells induced by interferon by mediating ISGylation of proteins involved in innate immunity, such as CGAS, IRF3, IFIH1/MDA5 and STING1. Catalyzes ISGylation of …

**Summary**, from NCBI Gene [51191](https://www.ncbi.nlm.nih.gov/gene/51191):

> This gene is a member of the HERC family of ubiquitin ligases and encodes a protein with a HECT domain and five RCC1 repeats. Pro-inflammatory cytokines upregulate expression of this gene in endothelial cells. The protein localizes to the cytoplasm and perinuclear region and functions as an interferon-induced E3 protein ligase that mediates ISGylation of protein targets. The protein also acts as a modulator of the antiviral immune response. The gene lies in a cluster of HERC family genes on …

**Accessions** — [HGNC:24368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24368) · Entrez [51191](https://www.ncbi.nlm.nih.gov/gene/51191) · UniProt [Q9UII4](https://www.uniprot.org/uniprotkb/Q9UII4) · Ensembl [ENSG00000138646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138646)

## Data

Gene col 6203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6203); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6203]; `tensor/DDL_lfc|DDL_z.npy` [6203]; `embed/gene_vectors.npy` [6203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6203 or target_col == 6203). Every well: [[HERC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
