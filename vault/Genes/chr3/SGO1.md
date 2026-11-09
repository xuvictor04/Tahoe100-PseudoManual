---
symbol: "SGO1"
type: "gene"
col: 5003
ensembl_id: "ENSG00000129810"
name: "shugoshin 1"
location: "3p24.3"
module: 22
arm: "+"
pooled_cpm: 27.91
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/022", "written"]
generated_by: "tahoemap"
---

# SGO1

*shugoshin 1* — 3p24.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SGO1 encodes shugoshin 1, the mitotic protein that shields centromeric cohesin from premature removal so sister chromatids stay paired until anaphase.

## What it is

Shugoshin is recruited to centromeres by the Bub1-phosphorylated H2A-T120 mark and by contacts near CENP-A, and brings the phosphatase PP2A-B56 to the right place. PP2A dephosphorylates sororin and the cohesin subunit SA2, blocking the Wapl- and separase-driven cohesin release that strips cohesin from chromosome arms in prophase; Cdk1 phosphorylation of Sgo1 in mitosis switches on its direct cohesin binding, making the protection mitosis-specific. Loss produces premature sister-chromatid separation, missegregation and aneuploidy, and Sgo1 also participates in kinetochore tension sensing. Clinically, a homozygous founder variant causes CAID syndrome — chronic atrial and intestinal dysrhythmia — a cohesinopathy of sinus-node and gut pacemaker tissue, with accelerated cycling and increased senescence in patient fibroblasts.

## What is uncertain

Whether "p53 target" means anything direct here. I know of no evidence for p53 occupancy at the SGO1 promoter, and the whole mitotic module — [[KIF11]], [[HJURP]], [[CENPN]] and this gene together — moves as a block, the signature of indirect repression through the cell cycle rather than gene-specific regulation. In the earlier MG53/p53 study its p53-programme membership was also only partially stable across cross-fitting folds, so it sits nearer the selection threshold than the strongly repressed cell-cycle genes. Treating its decline as evidence about p53's direct output would be over-reading.

## References

- Kitajima et al., 2006, Nature — showed that shugoshin collaborates with PP2A to protect centromeric cohesin.
- Liu, Rankin & Yu, 2013, Nature Cell Biology — Cdk-mediated mitotic phosphorylation of Sgo1 activates its direct cohesin binding.
- Chetaille et al., 2014, Nature Genetics — a homozygous SGO1 founder mutation causes CAID syndrome, a cohesinopathy of heart and gut rhythm.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +12.7, q 5e-34, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~93% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.37× (z +4.0, q 0.004, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.468× (z -8.7, q 7e-16, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.563× (z -3.9, q 0.009, down in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (A-427 0.241×, A498 0.291×, LoVo 0.277×, H4 0.172×, …; ⚠ cell-cycle shift, explains ~90% of this change); [[Selinexor (drug)]] 0.5 µM in 2 lines (LS 180 0.112×, A498 0.223×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.386×, H4 0.208×); [[Amsacrine (drug)]] 5 µM in 2 lines (LS 180 0.225×, A498 0.421×); [[Vilanterol (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0693×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC4]] (+0.94, fdr 7e-06), [[NDC80]] (+0.94, fdr 7e-06), [[MKI67]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **2.01×** | +12.7 | 5e-34 | 36/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.03×** | +9.1 | 2e-17 | 32/43 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.05×** | +8.8 | 2e-16 | 29/35 (A549, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **1.85×** | +7.9 | 4e-13 | 37/45 (HT-29, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.89×** | +7.9 | 5e-13 | 38/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.35×** | +5.5 | 4e-06 | 30/47 (NCI-H1573, NCI-H23, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.44×** | +4.7 | 2e-04 | 23/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.004 | 18/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +3.9 | 0.007 | 21/46 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +3.4 | 0.038 | 18/40 (NCI-H2347, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.3 | 0.042 | 21/46 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.049 | 10/46 (SW 900, HT-29, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +3.2 | 0.071 | 14/46 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.073 | 15/47 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.27×** | +3.1 | 0.083 | 16/47 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.085 | 12/47 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.087 | 12/46 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5003.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (A-427 0.241×, A498 0.291×, LoVo 0.277×, H4 0.172×, …; ⚠ cell-cycle shift, explains ~90% of this change); [[Selinexor (drug)]] 0.5 µM in 2 lines (LS 180 0.112×, A498 0.223×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.386×, H4 0.208×); [[Amsacrine (drug)]] 5 µM in 2 lines (LS 180 0.225×, A498 0.421×); [[Vilanterol (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.468×** | -8.7 | 7e-16 | 34/47 (KATO III, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.619×** | -8.7 | 7e-16 | 30/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.628×** | -6.0 | 4e-07 | 33/47 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.462×** | -5.2 | 3e-05 | 27/40 (KATO III, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.684×** | -4.9 | 1e-04 | 29/46 (A-172, C32, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.529×** | -4.3 | 0.002 | 20/47 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -3.9 | 0.009 | 24/46 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.771×** | -3.3 | 0.059 | 18/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.3 | 0.067 | 18/46 (H4, Hs 766T, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.838× | -3.2 | 0.074 | 19/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -3.2 | 0.074 | 17/47 (SW1417, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.84 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.5 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.8) ⚠ cell-cycle shift, explains ~93% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.159× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.231× (z -9.3) |
| [[H4 (line)]] | wt | 21.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.208× (z -9.3) |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.105× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.225× (z -10.2) |
| [[A-427 (line)]] | wt | 50.5 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.241× (z -15.6) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.386× (z -10.4) |
| [[A498 (line)]] | wt | 24.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.291× (z -12.1) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.421× (z -8.5) |
| [[A549 (line)]] | wt | 25.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.1) ⚠ cell-cycle shift, explains ~93% of this change | [[Selinexor (drug)]] 5 µM 0.395× (z -9.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.185× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.212× (z -9.0) |
| [[PANC-1 (line)]] | alt | 27.9 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +16.9) ⚠ cell-cycle shift, explains ~93% of this change | [[Ixazomib citrate (drug)]] 0.5 µM 0.394× (z -8.5) |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.3) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.152× (z -9.1) |
| [[HS-578T (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +13.6) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.5) ⚠ cell-cycle shift, explains ~93% of this change | [[Selinexor (drug)]] 5 µM 0.328× (z -10.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[RKO (line)]] | wt | 33.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.8) ⚠ cell-cycle shift, explains ~93% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~74% of this change |
| [[C32 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.187× (z -8.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0693× (z -10.0) |
| [[J82 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +14.8) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[KATO III (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.180× (z -11.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[LoVo (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -11.9) ⚠ cell-cycle shift, explains ~90% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.8) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.2) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.9) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SNU-423 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +11.0) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0520× (z -9.7) |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC4]] | +0.94 | +0.93 / +0.92 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 617 |
| [[NDC80]] | +0.94 | +0.91 / +0.93 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 932 |
| [[MKI67]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | STRING 610 |
| [[NCAPG]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 719 |
| [[KNL1]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 793 |
| [[CKAP2L]] | +0.91 | +0.87 / +0.90 | both halves | 7e-06 | STRING 747 |
| [[KIF4A]] | +0.89 | +0.89 / +0.85 | both halves | 7e-06 | STRING 698 |
| [[KIF11]] | +0.89 | +0.86 / +0.88 | both halves | 7e-06 | STRING 841 |
| [[TPX2]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | pathway: G2/M Transition; STRING 611 |
| [[KIF15]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | STRING 723 |
| [[KIF18A]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 862 |
| [[CDK1]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 902 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises SGO1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without E2F8 | 0.021 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises SGO1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises SGO1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises SGO1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without NDC80 | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises SGO1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without FAM72D | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[PBK]] | C | PBK activity raises SGO1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without PBK | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises SGO1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.80× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.6, -55.6); signed map (-49.2, -44.7). **Vector** length 133, 43.0% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.71 to 60); *DREAM G2/M down* (control, mean cos +0.79 to 28); *E2F targets* (hallmark, mean cos +0.68 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +8.6 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +7.5 | +7.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.3 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | +3.3 | +7.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +4.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.9 | +3.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.5 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -6.3 | -8.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.1 | -4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | -4.3 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | shugoshin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:20,160,593-20,186,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-BR-85; previously SGOL1 |
| Gene groups (HGNC) | Shugoshin family |
| Reactome | 20 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5FBB7](https://www.uniprot.org/uniprotkb/Q5FBB7) (Shugoshin 1):

> Plays a central role in chromosome cohesion during mitosis by preventing premature dissociation of cohesin complex from centromeres after prophase, when most of cohesin complex dissociates from chromosomes arms. May act by preventing phosphorylation of the STAG2 subunit of cohesin complex at the centromere, ensuring cohesin persistence at centromere until cohesin cleavage by ESPL1/separase at anaphase. Essential for proper chromosome segregation during mitosis and this function requires …

**Summary**, from NCBI Gene [151648](https://www.ncbi.nlm.nih.gov/gene/151648):

> The protein encoded by this gene is a member of the shugoshin family of proteins. This protein is thought to protect centromeric cohesin from cleavage during mitotic prophase by preventing phosphorylation of a cohesin subunit. Reduced expression of this gene leads to the premature loss of centromeric cohesion, mis-segregation of sister chromatids, and mitotic arrest. Evidence suggests that this protein also protects a small subset of cohesin found along the length of the chromosome arms during …

**Accessions** — [HGNC:25088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25088) · Entrez [151648](https://www.ncbi.nlm.nih.gov/gene/151648) · UniProt [Q5FBB7](https://www.uniprot.org/uniprotkb/Q5FBB7) · Ensembl [ENSG00000129810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129810)

## Data

Gene col 5003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5003); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5003]; `tensor/DDL_lfc|DDL_z.npy` [5003]; `embed/gene_vectors.npy` [5003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5003 or target_col == 5003). Every well: [[SGO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SGO1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
