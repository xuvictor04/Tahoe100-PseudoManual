---
symbol: "SMAD4"
type: "gene"
col: 6561
ensembl_id: "ENSG00000141646"
name: "SMAD family member 4"
location: "18q21.2"
module: 69
arm: "+"
pooled_cpm: 99.84
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/069", "written"]
generated_by: "tahoemap"
---

# SMAD4

*SMAD family member 4* — 18q21.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SMAD4 is the shared partner SMAD through which both TGF-beta and BMP signals reach the nucleus, and one of the most frequently deleted tumour suppressors in gastrointestinal cancer.

## What it is

Receptor-activated SMADs — SMAD2/3 for TGF-beta, SMAD1/5/8 for BMP — are phosphorylated at their C-termini, bind SMAD4 through MH2 contacts and accumulate in the nucleus as a complex whose weak MH1 DNA binding is given specificity by partners such as FOX and RUNX proteins. Because it is common to both branches, losing SMAD4 removes both. Biallelic inactivation occurs in roughly half of pancreatic ductal adenocarcinomas, where the gene was identified as DPC4, and is common in colorectal cancer; germline loss-of-function causes juvenile polyposis, while mutation at a single MH2 codon causes the gain-of-function Myhre syndrome. TGF-beta's cytostatic arm converges on CDKN1A induction and MYC repression, where it meets p53 biology.

## What is uncertain

A substantial minority of lines in a pooled cancer panel are SMAD4-deleted, so inferred "SMAD4 activity" is partly a readout of genotype heterogeneity rather than signalling. Its regulon overlaps SMAD2/3 and AP-1 sets by construction and cannot separate them.

## References

- Hahn et al., 1996, Science — identified DPC4/SMAD4 as a candidate tumour suppressor homozygously deleted in pancreatic cancer.
- Howe et al., 1998, Science — germline SMAD4 mutations cause juvenile polyposis.
- Le Goff et al., 2011, Nature Genetics — mutations at a single codon in the MH2 domain cause Myhre syndrome.
- Massague, 2008, Cell — review of TGF-beta signalling in cancer, including the cytostatic programme.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.00× (z +6.4, q 6e-08, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.409× (z -15.9, q 0e+00, down in 43 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.586× (z -9.5, q 3e-19, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIG2]] (+0.62, fdr 7e-06), [[ZNF451]] (+0.59, fdr 1e-05), [[DUSP11]] (+0.55, fdr 1e-05); moves opposite to [[CMIP]] (-0.53, fdr 5e-05), [[EPHB2]] (-0.53, fdr 3e-05), [[CHST11]] (-0.49, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[EFHD2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +6.4 | 6e-08 | 32/44 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.1 | 3e-07 | 31/45 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.60×** | +4.4 | 0.002 | 30/45 (A498, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.7 | 0.034 | 22/43 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.13× | +3.0 | 0.29 | 2/44 (LOX-IMVI, HT-29) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.409×** | -15.9 | 0e+00 | 43/45 (NCI-H1573, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.441×** | -14.0 | 5e-42 | 39/41 (HCT15, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.428×** | -13.9 | 9e-42 | 38/42 (HS-578T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.573×** | -9.9 | 6e-21 | 43/44 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.585×** | -9.5 | 2e-19 | 41/44 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.586×** | -9.5 | 3e-19 | 41/44 (AN3 CA, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.591×** | -9.3 | 8e-19 | 41/44 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.715×** | -8.4 | 3e-15 | 33/45 (A549, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -7.3 | 2e-11 | 40/44 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -7.1 | 8e-11 | 36/44 (HOP62, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -5.6 | 9e-07 | 35/44 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.802×** | -5.5 | 2e-06 | 24/44 (hTERT-HPNE, SNU-423, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -5.0 | 2e-05 | 0/46 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.756×** | -4.7 | 8e-05 | 30/43 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.633×** | -4.2 | 9e-04 | 23/44 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.645×** | -4.1 | 0.002 | 30/44 (NCI-H2347, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.8 | 0.005 | 22/44 (HOP62, A549, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -3.5 | 0.015 | 24/44 (RKO, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.4 | 0.018 | 15/44 (HS-578T, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.041 | 20/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.846× | -2.9 | 0.082 | 14/44 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.730×** | -2.9 | 0.085 | 18/44 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 73.0 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -10.4) |
| [[A549 (line)]] | wt | 118 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -17.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.447× (z -9.3) |
| [[HS-578T (line)]] | alt | 143 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -18.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 163 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 87.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 107 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 198 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 107 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +8.7) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 64.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -8.7) |
| [[AN3 CA (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.282× (z -9.4) |
| [[J82 (line)]] | alt | 126 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 84.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -12.4) ⚠ toxic |
| [[C-33 A (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0988× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 118 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.39× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -14.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 119 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.45× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 73.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 98.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1088 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0753× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 98.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.79 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2]] | +0.62 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZNF451]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[DUSP11]] | +0.55 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[KLHDC2]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[NUBP2]] | +0.53 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ENY2]] | +0.53 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[TRIM23]] | +0.51 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[PCMTD1]] | +0.51 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MMUT]] | +0.51 | +0.58 / +0.53 | both halves | 1e-05 | STRING 423 |
| [[PAPOLG]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[C12orf76]] | +0.50 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[CAND1]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | -0.53 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[EPHB2]] | -0.53 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[CHST11]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CDC37]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[FOSL1]] | -0.47 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[RELT]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[SLC45A3]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[PRKCA]] | -0.45 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[ERCC1]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ABR]] | -0.44 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GPR39]] | -0.44 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[JUN]] | -0.43 | -0.47 / -0.40 | both halves | 5e-05 | STRING 989 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFHD2]] | C | SMAD4 activity lowers EFHD2's level | lines that do not express SMAD4 (4) vs lines expressing it (46) | 3.44× higher at baseline in the lines without SMAD4 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC26A11 |
| [[FHIP2A]] | C | SMAD4 activity raises FHIP2A's level | lines that do not express SMAD4 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without SMAD4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC26A11; its own permutation p |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -48.8); signed map (-12.4, 4.3). **Vector** length 86.4, 25.1% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +4.2 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.1 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:51,028,528-51,085,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPC4; previously MADH4 |
| Gene groups (HGNC) | SMAD family |
| Reactome | 40 pathways, smallest: Loss of Function of SMAD4 in Cancer; SMAD2/3 MH2 Domain Mutants in Cancer; SMAD4 MH2 Domain Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13485](https://www.uniprot.org/uniprotkb/Q13485) (SMAD family member 4):

> In muscle physiology, plays a central role in the balance between atrophy and hypertrophy. When recruited by MSTN, promotes atrophy response via phosphorylated SMAD2/4. MSTN decrease causes SMAD4 release and subsequent recruitment by the BMP pathway to promote hypertrophy via phosphorylated SMAD1/5/8. Acts synergistically with SMAD1 and YY1 in bone morphogenetic protein (BMP)-mediated cardiac-specific gene expression. Binds to SMAD binding elements (SBEs) (5'-GTCT/AGAC-3') within BMP response …

**Summary**, from NCBI Gene [4089](https://www.ncbi.nlm.nih.gov/gene/4089):

> This gene encodes a member of the Smad family of signal transduction proteins. Smad proteins are phosphorylated and activated by transmembrane serine-threonine receptor kinases in response to transforming growth factor (TGF)-beta signaling. The product of this gene forms homomeric complexes and heteromeric complexes with other activated Smad proteins, which then accumulate in the nucleus and regulate the transcription of target genes. This protein binds to DNA and recognizes an 8-bp palindromic …

**Accessions** — [HGNC:6770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6770) · Entrez [4089](https://www.ncbi.nlm.nih.gov/gene/4089) · UniProt [Q13485](https://www.uniprot.org/uniprotkb/Q13485) · Ensembl [ENSG00000141646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141646)

## Data

Gene col 6561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6561); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6561]; `tensor/DDL_lfc|DDL_z.npy` [6561]; `embed/gene_vectors.npy` [6561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6561 or target_col == 6561). Every well: [[SMAD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SMAD4.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
