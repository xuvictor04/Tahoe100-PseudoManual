---
symbol: "DNMT3A"
type: "gene"
col: 4117
ensembl_id: "ENSG00000119772"
name: "DNA methyltransferase 3 alpha"
location: "2p23.3"
module: 46
arm: "+"
pooled_cpm: 45.14
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046", "written"]
generated_by: "tahoemap"
---

# DNMT3A

*DNA methyltransferase 3 alpha* — 2p23.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> DNMT3A is a de novo DNA methyltransferase that writes new CpG methylation, and one of the most frequently mutated genes in myeloid disease.

## What it is

With DNMT3B, DNMT3A methylates CpGs that were previously unmethylated; DNMT1 then copies the pattern through replication. Two reader domains aim it: an ADD domain that binds histone H3 only when K4 is unmethylated, autoinhibiting catalysis until it does, and a PWWP domain that reads H3K36 methylation and aims the enzyme at gene bodies and heterochromatin. Loss in mouse stem cells expands the stem compartment and impairs differentiation; the human R882H hotspot acts dominant-negatively by disrupting tetramer formation; and DNMT3A is the most common lesion in age-related clonal haematopoiesis. Germline mutation causes an overgrowth and intellectual-disability syndrome.

## What is uncertain

Calling DNMT3A a transcription factor is a stretch: it has no sequence specificity of its own, and its curated regulon is assembled from genes whose expression tracks methylation, so the sign attached to it is hard to read. Two confounds: the compound panel includes DNA methyltransferase inhibitors, which move this pathway directly, and methylation changes slowly relative to a 24 h readout.

## References

- Okano et al., 1999, Cell — Dnmt3a and Dnmt3b are required for de novo methylation and mammalian development.
- Ley et al., 2010, New England Journal of Medicine — identified recurrent DNMT3A mutations in acute myeloid leukaemia.
- Challen et al., 2011, Nature Genetics — Dnmt3a loss expands haematopoietic stem cells and blocks differentiation.
- Jaiswal et al., 2014, New England Journal of Medicine — age-related clonal haematopoiesis, with DNMT3A the most common driver.
- Tatton-Brown et al., 2014, Nature Genetics — germline DNMT3A mutations cause an overgrowth syndrome with intellectual disability.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +8.2, q 2e-13, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (LoVo 2.91×, A498 2.49×, NCI-H460 2.25×, RKO 2.79×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.78×, NCI-H23 2.22×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.90×; ⚠ cell-cycle shift, explains ~79% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.264× (z -27.0, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF2]] (+0.70, fdr 7e-06), [[BRD1]] (+0.68, fdr 1e-05), [[NACC2]] (+0.66, fdr 1e-05); moves opposite to [[RADX]] (-0.60, fdr 3e-05), [[POT1]] (-0.59, fdr 1e-04), [[SKIC3]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRRN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (LoVo 2.91×, A498 2.49×, NCI-H460 2.25×, RKO 2.79×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.78×, NCI-H23 2.22×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.90×; ⚠ cell-cycle shift, explains ~79% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.2 | 2e-13 | 28/47 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.4 | 0.11 | 8/47 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.11 | 17/46 (HOP62, HEC-1-A, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.11 | 12/47 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.11 | 0/48 | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.18× | +3.1 | 0.15 | 9/47 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.16× | +3.0 | 0.20 | 8/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.264×** | -27.0 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.270×** | -26.5 | 0e+00 | 46/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.367×** | -20.3 | 0e+00 | 47/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -12.7 | 6e-35 | 45/48 (LOX-IMVI, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.588×** | -8.0 | 1e-13 | 34/46 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.479×** | -7.8 | 6e-13 | 36/47 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -7.6 | 3e-12 | 29/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.672×** | -7.4 | 9e-12 | 28/43 (A-427, NCI-H23, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -7.3 | 2e-11 | 32/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.777×** | -7.2 | 4e-11 | 25/47 (J82, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -6.0 | 1e-07 | 25/47 (C32, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.775×** | -5.1 | 1e-05 | 24/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -5.1 | 1e-05 | 22/47 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -5.1 | 1e-05 | 22/47 (C32, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.619×** | -5.1 | 2e-05 | 20/36 (HEC-1-A, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -5.0 | 2e-05 | 25/47 (C32, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.628×** | -4.9 | 3e-05 | 25/47 (A498, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.722×** | -4.7 | 9e-05 | 20/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.657×** | -4.4 | 3e-04 | 23/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.669×** | -4.2 | 6e-04 | 19/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 98.6 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.164× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 50.8 | 1 | 12 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.140× (z -24.0) |
| [[A549 (line)]] | wt | 58.7 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.200× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 65.2 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -18.1) |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -10.7) |
| [[A-427 (line)]] | wt | 70.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.170× (z -20.2) |
| [[A498 (line)]] | wt | 45.1 | 2 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -13.1) |
| [[J82 (line)]] | alt | 33.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 74.7 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.270× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 73.9 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -23.1) |
| [[HEC-1-A (line)]] | alt | 41.1 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.241× (z -15.0) |
| [[LoVo (line)]] | wt | 46.3 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.100× (z -21.9) |
| [[HOP62 (line)]] | alt | 36.2 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 66.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -14.0) |
| [[RKO (line)]] | wt | 43.4 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.291× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 61.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -17.0) |
| [[SNU-1 (line)]] | wt | 80.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.182× (z -13.5) |
| [[SW480 (line)]] | alt | 48.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -25.4) |
| [[AN3 CA (line)]] | alt | 76.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.129× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -14.4) |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -16.7) |
| [[C-33 A (line)]] | alt | 66.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0881× (z -21.7) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 51.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -17.1) |
| [[SHP-77 (line)]] | alt | 72.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -17.6) |
| [[SW1417 (line)]] | alt | 50.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -15.6) |
| [[SW48 (line)]] | wt | 66.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -14.7) |
| [[A-172 (line)]] | wt | 54.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -14.4) |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.5) |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -10.7) |
| [[SW 900 (line)]] | alt | 48.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -11.1) |
| [[HCT15 (line)]] | alt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.8) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF2]] | +0.70 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes |
| [[BRD1]] | +0.68 | +0.59 / +0.53 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes |
| [[NACC2]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KIF27]] | +0.62 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[WTIP]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SETD1B]] | +0.62 | +0.46 / +0.49 | both halves | 3e-05 | pathway: Chromatin modifying enzymes |
| [[ZFTRAF1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CRTC3]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HDAC7]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 431 |
| [[ATAD2B]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PHLPP2]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[HDGFL3]] | +0.59 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RADX]] | -0.60 | -0.43 / -0.51 | both halves | 3e-05 | same gene group |
| [[POT1]] | -0.59 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.58 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PLA2G12A]] | -0.57 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SKP2]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RFC1]] | -0.55 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ELP1]] | -0.54 | -0.38 / -0.39 | both halves | 7e-05 | pathway: Chromatin modifying enzymes |
| [[PTCD3]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[VTA1]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[STARD3NL]] | -0.54 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ATP5F1C]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[FIGNL1]] | -0.53 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRN2]] | B | LRRN2 activity raises DNMT3A's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without LRRN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[SOGA1]] | C | SOGA1 activity raises DNMT3A's level | lines that do not express SOGA1 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without SOGA1 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, ODAD4, GGT7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.5, 12.3); signed map (8.8, -4.9). **Vector** length 109, 30.5% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.8 | -12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -26.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -20.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -27.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -4.7 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA methyltransferase 3 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:25,227,855-25,342,590 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PWWP domain containing; MicroRNA protein coding host genes; 7BS C5-cytosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 13 pathways, smallest: SUMOylation of DNA methylation proteins; DNA methylation; Defective pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6K1](https://www.uniprot.org/uniprotkb/Q9Y6K1) (DNA):

> DNA (cytosine-5)-methyltransferase that mediates genome-wide de novo methylation and which is essential for the establishment of DNA methylation patterns during development. It modifies DNA in a non-processive manner and methylates both CpG and non-CpG sites. Modifies DNA at CpG sites with selectivity for residues flanking the target CpG site at positions -2 and +2. Preferentially methylates DNA linker regions between two nucleosomal cores and is inhibited by histone H1 (By similarity). DNA …

**Summary**, from NCBI Gene [1788](https://www.ncbi.nlm.nih.gov/gene/1788):

> CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase that is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes to the cytoplasm and nucleus and its expression is developmentally regulated. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:2978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2978) · Entrez [1788](https://www.ncbi.nlm.nih.gov/gene/1788) · UniProt [Q9Y6K1](https://www.uniprot.org/uniprotkb/Q9Y6K1) · Ensembl [ENSG00000119772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119772)

## Data

Gene col 4117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4117); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4117]; `tensor/DDL_lfc|DDL_z.npy` [4117]; `embed/gene_vectors.npy` [4117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4117 or target_col == 4117). Every well: [[DNMT3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/DNMT3A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
