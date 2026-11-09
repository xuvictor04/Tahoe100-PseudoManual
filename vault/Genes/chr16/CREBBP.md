---
symbol: "CREBBP"
type: "gene"
col: 79
ensembl_id: "ENSG00000005339"
name: "CREB binding lysine acetyltransferase"
location: "16p13.3"
module: 95
arm: "+"
pooled_cpm: 200.56
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/095", "written"]
generated_by: "tahoemap"
---

# CREBBP

*CREB binding lysine acetyltransferase* — 16p13.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> CREBBP encodes CBP, a lysine acetyltransferase and transcriptional coactivator that many DNA-binding factors — p53 among them — depend on to reach chromatin.

## What it is

CBP and its paralogue p300 share a domain layout built for brokering: TAZ1 and TAZ2 zinc-binding regions, a KIX domain, a bromodomain and a central acetyltransferase. CBP acetylates histones — H3K27 at active enhancers — and many non-histone substrates, including lysines in the p53 C-terminus, where acetylation stabilises p53 on DNA and raises target induction. Because CBP is shared among many pathways and limited in amount, competition for it is regulatory. Germline heterozygous loss causes Rubinstein-Taybi syndrome; somatic inactivating mutations are frequent in B-cell lymphoma, relapsed acute lymphoblastic leukaemia and bladder cancer. CBP and p300 are partly redundant.

## What is uncertain

Whether "CREBBP activity" is meaningful here is the first question. Its regulon in this collection is small and heterogeneous, so a coherent rise across it may report general enhancer acetylation rather than anything CBP-specific — which is also why its score is collinear with [[TP53]] and [[EP300]]. CBP mRNA is a poor proxy for function, since the biology is competition at the protein level.

## References

- Petrij et al., 1995, Nature — mutations in CBP cause Rubinstein-Taybi syndrome.
- Gu & Roeder, 1997, Cell — acetylation of the p53 C-terminal domain by p300 activates its sequence-specific DNA binding.
- Avantaggiati et al., 1997, Cell — p300/CBP is recruited into p53-dependent transcriptional responses.
- Pasqualucci et al., 2011, Nature — recurrent inactivating mutations of CREBBP and EP300 in B-cell lymphoma.
- Mullighan et al., 2011, Nature — CREBBP mutations are enriched at relapse in acute lymphoblastic leukaemia.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +31.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.324× (z -33.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EP300]] (+0.81, fdr 7e-06), [[INO80D]] (+0.79, fdr 7e-06), [[MED13]] (+0.77, fdr 1e-05); moves opposite to [[WASF3]] (-0.71, fdr 1e-05), [[FCHO1]] (-0.69, fdr 3e-05), [[ST6GALNAC4]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 79.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +31.0 | 0e+00 | 47/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +20.6 | 0e+00 | 47/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +17.6 | 0e+00 | 45/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +14.1 | 8e-43 | 44/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +12.9 | 9e-36 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +12.5 | 8e-34 | 39/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +12.3 | 9e-33 | 44/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +10.7 | 1e-24 | 27/49 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +9.6 | 5e-20 | 33/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +9.0 | 2e-17 | 31/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +7.9 | 2e-13 | 35/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +7.4 | 8e-12 | 38/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.6 | 1e-09 | 27/50 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +5.8 | 4e-07 | 27/48 (H4, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +5.5 | 2e-06 | 23/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +4.9 | 3e-05 | 19/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +4.5 | 2e-04 | 18/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 79.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.324×** | -33.7 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.334×** | -32.8 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.337×** | -32.6 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.470×** | -22.6 | 0e+00 | 47/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.486×** | -21.6 | 0e+00 | 46/49 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -18.0 | 0e+00 | 41/44 (AN3 CA, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -17.5 | 0e+00 | 47/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.674×** | -16.7 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.566×** | -15.7 | 0e+00 | 40/45 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -11.0 | 3e-26 | 43/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -9.7 | 1e-20 | 36/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.484×** | -9.4 | 2e-19 | 46/49 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.848× | -5.0 | 3e-05 | 18/48 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -4.0 | 0.003 | 0/50 | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.003 | 24/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.912× | -3.9 | 0.003 | 3/48 (AsPC-1, BT-474, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.892× | -3.4 | 0.019 | 7/49 (SNU-423, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 79. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 189 | 9 (1 ⚠) | 11 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -30.0) |
| [[LS 180 (line)]] | wt | 222 | 9 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +21.7) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -18.1) |
| [[LoVo (line)]] | wt | 306 | 8 (2 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +26.8) | [[Panobinostat (drug)]] 5 µM 0.264× (z -26.8) |
| [[NCI-H1792 (line)]] | alt | 191 | 7 (1 ⚠) | 9 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.42× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.251× (z -22.2) |
| [[AsPC-1 (line)]] | alt | 294 | 7 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +23.0) | [[Panobinostat (drug)]] 5 µM 0.221× (z -24.1) |
| [[HEC-1-A (line)]] | alt | 192 | 8 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.337× (z -21.2) |
| [[LOX-IMVI (line)]] | wt | 279 | 4 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -24.5) |
| [[MIA PaCa-2 (line)]] | alt | 190 | 4 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.205× (z -26.8) |
| [[NCI-H1573 (line)]] | alt | 325 | 6 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.208× (z -26.7) |
| [[NCI-H460 (line)]] | wt | 169 | 5 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +20.2) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -20.5) |
| [[A498 (line)]] | wt | 224 | 5 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +27.1) | [[Panobinostat (drug)]] 5 µM 0.332× (z -18.8) |
| [[C32 (line)]] | wt | 182 | 6 | 7 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.47× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.358× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 205 | 4 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -21.9) |
| [[HS-578T (line)]] | alt | 119 | 9 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.386× (z -14.9) |
| [[KATO III (line)]] | alt | 286 | 5 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +19.3) | [[Panobinostat (drug)]] 5 µM 0.247× (z -22.8) |
| [[Panc 03.27 (line)]] | alt | 164 | 4 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -19.7) |
| [[SNU-423 (line)]] | alt | 210 | 3 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.1) | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -20.6) |
| [[COLO 205 (line)]] | alt | 230 | 6 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +19.7) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -19.0) |
| [[HT-29 (line)]] | alt | 217 | 2 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.3) | [[Belinostat (drug)]] 5 µM 0.268× (z -22.1) |
| [[RKO (line)]] | wt | 224 | 5 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.373× (z -14.4) |
| [[SW48 (line)]] | wt | 228 | 6 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 221 | 2 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.367× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 130 | 4 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +19.0) | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -20.6) |
| [[SW 900 (line)]] | alt | 168 | 4 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.7) |
| [[A549 (line)]] | wt | 184 | 3 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -14.6) |
| [[H4 (line)]] | wt | 146 | 6 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.7) |
| [[Hs 766T (line)]] | wt | 182 | 3 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.340× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 177 | 2 | 8 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +17.0) | [[Belinostat (drug)]] 5 µM 0.371× (z -15.1) |
| [[SNU-1 (line)]] | wt | 265 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.352× (z -14.2) |
| [[A-172 (line)]] | wt | 177 | 3 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.385× (z -17.0) |
| [[HOP62 (line)]] | alt | 135 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -19.7) |
| [[PANC-1 (line)]] | alt | 163 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 159 | 4 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +16.6) | [[Belinostat (drug)]] 5 µM 0.382× (z -13.4) |
| [[BT-474 (line)]] | alt | 163 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.5) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -15.8) |
| [[HCT15 (line)]] | alt | 306 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.277× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 202 | 1 | 7 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.201× (z -26.5) |
| [[SW1417 (line)]] | alt | 225 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -20.2) |
| [[A-427 (line)]] | wt | 190 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -19.1) |
| [[C-33 A (line)]] | alt | 234 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 198 | 1 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.241× (z -19.3) |
| [[J82 (line)]] | alt | 183 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -15.9) |
| [[SHP-77 (line)]] | alt | 113 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -11.0) |
| [[AN3 CA (line)]] | alt | 256 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0418× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.356× (z -11.9) |
| [[CHP-212 (line)]] | wt | 189 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.329× (z -9.5) |
| [[SW 1271 (line)]] | alt | 222 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 79), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP300]] | +0.81 | +0.65 / +0.78 | both halves | 7e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[INO80D]] | +0.79 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MED13]] | +0.77 | +0.57 / +0.65 | both halves | 1e-05 | pathway: Adipogenesis; STRING 631 |
| [[BAZ2B]] | +0.76 | +0.70 / +0.61 | both halves | 7e-06 | same gene group; STRING 473 |
| [[ASH1L]] | +0.74 | +0.66 / +0.62 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 478 |
| [[ZFX]] | +0.73 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[AP5S1]] | +0.73 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ANKHD1-EIF4EBP3]] | +0.73 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[ARID1B]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers; STRING 585 |
| [[UNK]] | +0.72 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[EFCAB2]] | +0.72 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.72 | +0.61 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.71 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.69 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.46 / -0.47 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[IMPDH1]] | -0.66 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[KIF21B]] | -0.65 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD27]] | -0.65 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RNF216P1]] | -0.65 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | -0.64 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PRR5]] | -0.64 | -0.56 / -0.51 | both halves | 1e-05 | pathway: Regulation of T cell activation by CD28 family |
| [[ANXA6]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MAST3]] | -0.63 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[HACE1]] | -0.63 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CREBBP's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CREBBP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CREBBP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DYRK1A]] | C | DYRK1A's natural level strengthens CREBBP's drug response | DYRK1A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.18; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.4, 9.8); signed map (21.6, -17.5). **Vector** length 135, 51.6% of its response variance represented; |z| ≥ 3 in 1,555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.1 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.9 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.7 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | -0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -11.3 | -22.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -11.1 | -17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -16.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -9.7 | -32.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.4 | -11.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -7.8 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CREB binding lysine acetyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,725,054-3,880,713 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RTS, CBP, KAT3A; previously RSTS |
| Gene groups (HGNC) | Zinc fingers ZZ-type; Lysine acetyltransferases; Bromodomain containing |
| Hallmark sets | APOPTOSIS |
| Reactome | 130 pathways, smallest: LRR FLII-interacting protein 1 (LRRFIP1) activates type I IFN production; NFE2L2 regulating ER-stress associated genes; NFE2L2 regulating inflammation associated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92793](https://www.uniprot.org/uniprotkb/Q92793) (Histone lysine acetyltransferase CREBBP):

> Acetylates histones, giving a specific tag for transcriptional activation. Mediates acetylation of histone H3 at 'Lys-18' and 'Lys-27' (H3K18ac and H3K27ac, respectively). Also acetylates non-histone proteins, like DDX21, FBL, IRF2, MAFG, NCOA3, POLR1E/PAF53 and FOXO1. Binds specifically to phosphorylated CREB and enhances its transcriptional activity toward cAMP-responsive genes. Acts as a coactivator of ALX1. Acts as a circadian transcriptional coactivator which enhances the activity of the …

**Summary**, from NCBI Gene [1387](https://www.ncbi.nlm.nih.gov/gene/1387):

> This gene is ubiquitously expressed and is involved in the transcriptional coactivation of many different transcription factors. First isolated as a nuclear protein that binds to cAMP-response element binding protein (CREB), this gene is now known to play critical roles in embryonic development, growth control, and homeostasis by coupling chromatin remodeling to transcription factor recognition. The protein encoded by this gene has intrinsic histone acetyltransferase activity and also acts as a …

**Accessions** — [HGNC:2348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2348) · Entrez [1387](https://www.ncbi.nlm.nih.gov/gene/1387) · UniProt [Q92793](https://www.uniprot.org/uniprotkb/Q92793) · Ensembl [ENSG00000005339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005339)

## Data

Gene col 79: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 79); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 79, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 79]; `tensor/DDL_lfc|DDL_z.npy` [79]; `embed/gene_vectors.npy` [79]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 79 or target_col == 79). Every well: [[CREBBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CREBBP.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
