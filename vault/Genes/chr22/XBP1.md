---
symbol: "XBP1"
type: "gene"
col: 1893
ensembl_id: "ENSG00000100219"
name: "X-box binding protein 1"
location: "22q12.1"
module: 49
arm: "+"
pooled_cpm: 63.54
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049", "written"]
generated_by: "tahoemap"
---

# XBP1

*X-box binding protein 1* — 22q12.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> XBP1 is the bZIP transcription factor of the IRE1 branch of the unfolded protein response, switched on not by transcription but by unconventional cytoplasmic splicing of its own mRNA.

## What it is

Under ER stress the kinase/endoribonuclease IRE1-alpha excises a 26-nucleotide intron from XBP1 mRNA; the frameshifted product, XBP1s, is a potent activator that induces ER chaperones, ERAD components and lipid-biosynthesis genes to expand secretory capacity. The unspliced form, XBP1u, encodes a short-lived protein that negatively regulates XBP1s and ATF6. The decisive step is therefore post-transcriptional, unusual among mammalian transcription factors and consequential for anything inferred from expression. XBP1 is essential for plasma-cell differentiation, where secretory load drives the pathway constitutively; in cancer it supports survival under hypoxia and proteotoxic stress, and IRE1/XBP1 is an active drug target in myeloma.

## What is uncertain

Gene-level counts cannot distinguish XBP1u from XBP1s: the two differ by 26 nucleotides and standard quantification collapses them, so XBP1's measured level says little about whether the pathway is on. The regulon score sidesteps this by reading targets instead, but those overlap heavily with [[ATF4]]-, ATF6- and NRF2-driven programmes, so attributing them to XBP1 specifically is weak. Reported links between XBP1 and p53 are not consistent across systems, and nothing here tests them.

## References

- Yoshida et al., 2001, Cell — showed XBP1 mRNA is spliced by IRE1 to produce the active transcription factor.
- Calfon et al., 2002, Nature — showed IRE1 couples ER stress to XBP1 processing and ER chaperone induction.
- Reimold et al., 2001, Nature — XBP1 is required for plasma-cell differentiation.
- Chen et al., 2014, Nature — XBP1 supports triple-negative breast cancer survival under hypoxic stress.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.70× (z +8.5, q 1e-14, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.341× (z -17.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB9]] (+0.66, fdr 7e-06), [[GCC1]] (+0.65, fdr 7e-06), [[DDIT3]] (+0.64, fdr 7e-06); moves opposite to [[HDAC1]] (-0.59, fdr 4e-05), [[ABI2]] (-0.54, fdr 3e-05), [[BCAP31]] (-0.53, fdr 7e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.5 | 1e-14 | 28/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.8 | 3e-09 | 2/49 (HOP62, CHP-212) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.5 | 2e-08 | 27/46 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.3 | 3e-08 | 29/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 0.001 | 27/47 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.3 | 0.001 | 23/45 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.003 | 22/47 (SW480, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.003 | 20/46 (hTERT-HPNE, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.1 | 0.003 | 26/47 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.9 | 0.007 | 21/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.008 | 16/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.010 | 22/47 (LoVo, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.020 | 22/48 (hTERT-HPNE, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.021 | 21/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.025 | 18/47 (SW 900, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.064 | 18/45 (RPMI-7951, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.341×** | -17.9 | 0e+00 | 44/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.345×** | -17.7 | 0e+00 | 43/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.395×** | -15.5 | 0e+00 | 43/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.459×** | -13.0 | 2e-36 | 41/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.459×** | -12.5 | 1e-33 | 34/38 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -10.8 | 4e-25 | 34/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.601×** | -8.5 | 2e-15 | 35/47 (LoVo, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.425×** | -7.5 | 6e-12 | 35/48 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -5.1 | 2e-05 | 27/47 (HT-29, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.829×** | -4.4 | 5e-04 | 18/47 (SNU-423, A-427, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -3.9 | 0.005 | 23/47 (Hs 766T, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.794×** | -3.7 | 0.010 | 23/46 (HS-578T, SW 1088, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.813×** | -3.5 | 0.024 | 19/46 (SHP-77, KATO III, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.677×** | -3.4 | 0.027 | 17/34 (SNU-1, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.028 | 20/47 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.032 | 14/47 (RKO, HS-578T, …) | top dose only | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.038 | 16/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.038 | 18/47 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.874× | -3.2 | 0.042 | 7/47 (SW48, A549, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.827×** | -3.2 | 0.044 | 19/48 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.830×** | -2.9 | 0.091 | 17/46 (LoVo, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 92.8 | 1 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.246× (z -18.4) |
| [[KATO III (line)]] | alt | 114 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 56.3 | 4 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.81× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.2) |
| [[HS-578T (line)]] | alt | 113 | 1 | 7 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.73× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.341× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 74.0 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.258× (z -13.6) |
| [[A498 (line)]] | wt | 86.0 | 1 | 6 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.58× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.333× (z -12.7) |
| [[COLO 205 (line)]] | alt | 96.4 | 3 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.74× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -9.1) |
| [[HT-29 (line)]] | alt | 140 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.260× (z -17.0) |
| [[SW 900 (line)]] | alt | 81.7 | 2 | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.09× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.271× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 86.6 | 2 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.68× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.196× (z -14.3) |
| [[HOP62 (line)]] | alt | 47.4 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 3.52× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.250× (z -12.4) |
| [[Hs 766T (line)]] | wt | 97.3 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 2.34× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.341× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.165× (z -13.6) |
| [[LS 180 (line)]] | wt | 81.6 | 1 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.236× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 64.1 | 2 | 3 | [[Harringtonine (drug)]] 0.5 µM 3.28× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 76.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -10.5) |
| [[SW480 (line)]] | alt | 50.0 | 2 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -13.5) |
| [[J82 (line)]] | alt | 51.6 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 2.54× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.314× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 64.4 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 3.56× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.289× (z -11.1) |
| [[SHP-77 (line)]] | alt | 97.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -8.8) |
| [[SNU-423 (line)]] | alt | 56.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.316× (z -10.0) |
| [[A-172 (line)]] | wt | 46.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.286× (z -10.8) |
| [[H4 (line)]] | wt | 61.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -10.6) |
| [[HCT15 (line)]] | alt | 77.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 50.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.401× (z -9.5) |
| [[RKO (line)]] | wt | 46.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -12.8) |
| [[SW1417 (line)]] | alt | 101 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.0) |
| [[A-427 (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0756× (z -11.5) |
| [[BT-474 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 64.3 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -9.4) |
| [[SW 1088 (line)]] | alt | 91.9 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0676× (z -9.8) |
| [[SW48 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB9]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 952 |
| [[GCC1]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[DDIT3]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 988 |
| [[SLC3A2]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[HAX1]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SLC35B1]] | +0.58 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[FICD]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[AKAP17A]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SEPHS2]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[IFRD1]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ALG2]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC1]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ABI2]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.53 | -0.37 / -0.52 | both halves | 7e-05 | STRING 477 |
| [[CPSF6]] | -0.52 | -0.23 / -0.60 | both halves | 5e-04 |  |
| [[TCF3]] | -0.52 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[HACD3]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MAPK1]] | -0.51 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[SLC23A2]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CLSTN1]] | -0.49 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ITGB1]] | -0.49 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[AP3M2]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF4]] | B | KLF4 activity raises XBP1's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without KLF4 | 0.041 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -1.1); signed map (-8.4, -8.7). **Vector** length 119, 35.2% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -5.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | -4.5 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -7.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | X-box binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:28,794,555-28,800,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously XBP2 |
| Gene groups (HGNC) | Basic leucine zipper proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P17861](https://www.uniprot.org/uniprotkb/P17861) (X-box-binding protein 1):

> Functions as a transcription factor during endoplasmic reticulum (ER) stress by regulating the unfolded protein response (UPR). Required for cardiac myogenesis and hepatogenesis during embryonic development, and the development of secretory tissues such as exocrine pancreas and salivary gland (By similarity). Involved in terminal differentiation of B lymphocytes to plasma cells and production of immunoglobulins. Modulates the cellular response to ER stress in a PIK3R-dependent manner. Binds to …

**Summary**, from NCBI Gene [7494](https://www.ncbi.nlm.nih.gov/gene/7494):

> This gene encodes a transcription factor that regulates MHC class II genes by binding to a promoter element referred to as an X box. This gene product is a bZIP protein, which was also identified as a cellular transcription factor that binds to an enhancer in the promoter of the T cell leukemia virus type 1 promoter. It may increase expression of viral proteins by acting as the DNA binding partner of a viral transactivator. It has been found that upon accumulation of unfolded proteins in the …

**Accessions** — [HGNC:12801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12801) · Entrez [7494](https://www.ncbi.nlm.nih.gov/gene/7494) · UniProt [P17861](https://www.uniprot.org/uniprotkb/P17861) · Ensembl [ENSG00000100219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100219)

## Data

Gene col 1893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1893); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1893]; `tensor/DDL_lfc|DDL_z.npy` [1893]; `embed/gene_vectors.npy` [1893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1893 or target_col == 1893). Every well: [[XBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/XBP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
