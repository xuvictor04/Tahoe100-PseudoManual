---
symbol: "CYP27B1"
type: "gene"
col: 3188
ensembl_id: "ENSG00000111012"
name: "cytochrome P450 family 27 subfamily B member 1"
location: "12q14.1"
module: 181
arm: "+"
pooled_cpm: 3.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# CYP27B1

*cytochrome P450 family 27 subfamily B member 1* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.12× (z +7.1, q 8e-10, up in 17 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.381× (z -4.8, q 9e-04, down in 9 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.0763×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.0718×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.120×); [[Vilanterol (drug)]] 0.5 µM in 1 line (PANC-1 0.0969×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL1]] (+0.71, fdr 7e-06, ⚠ same locus), [[NOL6]] (+0.66, fdr 7e-06), [[MATN1-AS1]] (+0.59, fdr 2e-05), [[ZPR1]] (+0.58, fdr 1e-05); moves opposite to [[NPEPPS]] (-0.60, fdr 1e-05), [[STK38]] (-0.55, fdr 3e-05), [[BTBD7]] (-0.54, fdr 1e-05).
> It is in [[Module 181]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +7.1 | 8e-10 | 17/34 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +6.7 | 4e-09 | 15/36 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.1 | 2e-07 | 15/31 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.2 | 3e-05 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +4.8 | 2e-04 | 12/45 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.5 | 7e-04 | 7/46 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.008 | 10/42 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +3.9 | 0.008 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.048 | 4/43 (SW480, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.066 | 2/43 (NCI-H2347, Panc 03.27) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.38× | +3.0 | 0.13 | 8/44 (HEC-1-A, NCI-H23, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3188.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.0763×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.0718×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.120×); [[Vilanterol (drug)]] 0.5 µM in 1 line (PANC-1 0.0969×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -4.8 | 9e-04 | 9/39 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.701× | -3.2 | 0.28 | 5/36 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.795× | -3.1 | 0.28 | 7/44 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.28 | 13/37 (C-33 A, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.60 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0763× (z -10.5) |
| [[A498 (line)]] | wt | 3.07 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0718× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 2.34 | 0 | 1 (1 ⚠) | — | [[Ribociclib (drug)]] 0.05 µM 0.0579× (z -8.7) ⚠ unreliable plate only; position not correctable |
| [[NCI-H1573 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0969× (z -8.6) |
| [[A-172 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.861 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL1]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 | STRING 782; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NOL6]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MATN1-AS1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ZPR1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MMP25]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRPM2]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CYB5D1]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[EMG1]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZNF597]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[AOC2]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 | pathway: Biological oxidations |
| [[KCNQ4]] | +0.55 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[THOC6]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[STK38]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[BTBD7]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MEGF9]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CRYZL1]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PIAS1]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 | STRING 651 |
| [[ZYG11B]] | -0.52 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[SEC24B]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 | pathway: Metabolism of steroids |
| [[PPP1R12B]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[IFT22]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[USP33]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[OSBPL9]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 | pathway: Metabolism of steroids |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.8, -33.8); signed map (-4.1, -43.9). **Vector** length 56.4, 7.58% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.1 | +2.7 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 27 subfamily B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,762,334-57,768,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYP1, P450c1; previously VDD1, PDDR |
| Gene groups (HGNC) | Cytochrome P450 family 27 |
| Reactome | 9 pathways, smallest: Vitamins; Vitamin D (calciferol) metabolism; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15528](https://www.uniprot.org/uniprotkb/O15528) (25-hydroxyvitamin D-1 alpha hydroxylase, mitochondrial):

> A cytochrome P450 monooxygenase involved in vitamin D metabolism and in calcium and phosphorus homeostasis. Catalyzes the rate-limiting step in the activation of vitamin D in the kidney, namely the hydroxylation of 25-hydroxyvitamin D3/calcidiol at the C1alpha-position to form the hormonally active form of vitamin D3, 1alpha,25-dihydroxyvitamin D3/calcitriol that acts via the vitamin D receptor (VDR). Has 1alpha-hydroxylase activity on vitamin D intermediates of the CYP24A1-mediated …

**Summary**, from NCBI Gene [1594](https://www.ncbi.nlm.nih.gov/gene/1594):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. The protein encoded by this gene localizes to the inner mitochondrial membrane where it hydroxylates 25-hydroxyvitamin D3 at the 1alpha position. This reaction synthesizes 1alpha,25-dihydroxyvitamin D3, the active form of vitamin D3, which binds to the vitamin D …

**Accessions** — [HGNC:2606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2606) · Entrez [1594](https://www.ncbi.nlm.nih.gov/gene/1594) · UniProt [O15528](https://www.uniprot.org/uniprotkb/O15528) · Ensembl [ENSG00000111012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111012)

## Data

Gene col 3188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3188); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3188]; `tensor/DDL_lfc|DDL_z.npy` [3188]; `embed/gene_vectors.npy` [3188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3188 or target_col == 3188). Every well: [[CYP27B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP27B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
