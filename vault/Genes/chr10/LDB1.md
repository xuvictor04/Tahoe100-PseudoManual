---
symbol: "LDB1"
type: "gene"
col: 12656
ensembl_id: "ENSG00000198728"
name: "LIM domain binding 1"
location: "10q24.32"
module: 126
arm: "+"
pooled_cpm: 16.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# LDB1

*LIM domain binding 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +12.4, q 3e-32, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.663× (z -4.9, q 6e-04, down in 26 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.702× (z -4.4, q 0.003, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USF1]] (+0.74, fdr 7e-06), [[INPPL1]] (+0.70, fdr 1e-05), [[BCL2L2]] (+0.68, fdr 1e-05); moves opposite to [[MT2A]] (-0.54, fdr 5e-05), [[ASL]] (-0.54, fdr 1e-04), [[KLF2]] (-0.53, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +12.4 | 3e-32 | 43/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +7.8 | 2e-12 | 35/48 (A549, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.6 | 8e-09 | 30/44 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.3 | 4e-08 | 29/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.6 | 4e-04 | 19/48 (A498, A-172, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.003 | 22/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.003 | 21/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.0 | 0.004 | 13/30 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.3 | 0.070 | 14/38 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.663×** | -4.9 | 6e-04 | 26/47 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -4.4 | 0.003 | 23/47 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.708×** | -4.3 | 0.003 | 18/48 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.021 | 22/48 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.751×** | -3.6 | 0.042 | 14/48 (A-172, SNU-1, …) | two highest doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.761× | -3.3 | 0.11 | 13/48 (SW 1271, LOX-IMVI, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.767× | -3.2 | 0.11 | 14/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.768× | -3.2 | 0.11 | 14/47 (SNU-423, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 3 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0710× (z -13.1) |
| [[A498 (line)]] | wt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +16.1) | — |
| [[A-172 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.0) | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.103× (z -8.7) |
| [[LoVo (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.7) | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0707× (z -10.3) |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USF1]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[INPPL1]] | +0.70 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CDK2AP1]] | +0.66 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ANP32A]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CIPC]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CERS2]] | +0.64 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MTA2]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NAXD]] | +0.63 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[PPM1A]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MSL3]] | +0.62 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[U2AF2]] | +0.61 | +0.38 / +0.57 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT2A]] | -0.54 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ASL]] | -0.54 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[KLF2]] | -0.53 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[PSMB1]] | -0.51 | -0.36 / -0.36 | both halves | 1e-04 | pathway: RUNX1 regulates transcription of genes involved in differentiation of HSCs |
| [[MT1X]] | -0.50 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LDB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers LDB1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[HLA-H]] | B | HLA-H activity lowers LDB1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.72× higher at baseline in the lines without HLA-H | 0.097 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens LDB1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.66× as strongly (z diff +1.05); strongest at Doxorubicin (hydrochloride) 5 µM: 1.45x vs 2.50x (z diff +2.8) | 0.127 over the table, 0.004 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, -22.0); signed map (-11.1, -34.8). **Vector** length 97.2, 20.6% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +12.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,106,489-102,120,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NLI, CLIM2 |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 10 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Cardiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U70](https://www.uniprot.org/uniprotkb/Q86U70) (LIM domain-binding protein 1):

> Binds to the LIM domain of a wide variety of LIM domain-containing transcription factors. May regulate the transcriptional activity of LIM-containing proteins by determining specific partner interactions. Plays a role in the development of interneurons and motor neurons in cooperation with LHX3 and ISL1. Acts synergistically with LHX1/LIM1 in axis formation and activation of gene expression. Acts with LMO2 in the regulation of red blood cell development, maintaining erythroid precursors in an …

**Summary**, from NCBI Gene [8861](https://www.ncbi.nlm.nih.gov/gene/8861):

> Enables LIM domain binding activity; RNA polymerase II-specific DNA-binding transcription factor binding activity; and enzyme binding activity. Involved in negative regulation of DNA-templated transcription and positive regulation of transcription by RNA polymerase II. Located in chromatin. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6532) · Entrez [8861](https://www.ncbi.nlm.nih.gov/gene/8861) · UniProt [Q86U70](https://www.uniprot.org/uniprotkb/Q86U70) · Ensembl [ENSG00000198728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198728)

## Data

Gene col 12656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12656); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12656]; `tensor/DDL_lfc|DDL_z.npy` [12656]; `embed/gene_vectors.npy` [12656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12656 or target_col == 12656). Every well: [[LDB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
