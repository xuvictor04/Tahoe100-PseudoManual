---
symbol: "TMEM147"
type: "gene"
col: 2644
ensembl_id: "ENSG00000105677"
name: "transmembrane protein 147"
location: "19q13.12"
module: 58
arm: "+"
pooled_cpm: 13.99
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM147

*transmembrane protein 147* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.53× (z +10.4, q 2e-22, up in 36 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 6.15×, SW480 6.65×, C32 12.9×, A-172 4.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.602× (z -4.9, q 5e-04, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.165×, RKO 0.207×, A498 0.332×); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0812×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APRT]] (+0.71, fdr 7e-06), [[C20orf27]] (+0.70, fdr 7e-06), [[MRPL12]] (+0.69, fdr 7e-06); moves opposite to [[CHD3]] (-0.59, fdr 3e-05), [[PAN2]] (-0.55, fdr 1e-04), [[RYR2]] (-0.53, fdr 6e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 6.15×, SW480 6.65×, C32 12.9×, A-172 4.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.53×** | +10.4 | 2e-22 | 36/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.49×** | +6.8 | 4e-09 | 24/28 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.34×** | +5.4 | 1e-05 | 26/31 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.91×** | +4.4 | 0.001 | 29/42 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.6 | 0.037 | 21/40 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 2.45× | +3.2 | 0.12 | 24/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.58× | +3.1 | 0.14 | 22/47 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.55× | +3.0 | 0.17 | 19/47 (HEC-1-A, HT-29, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.165×, RKO 0.207×, A498 0.332×); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0812×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -4.9 | 5e-04 | 29/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.8) |
| [[A-172 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 6.25 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.3) |
| [[SNU-423 (line)]] | alt | 7.70 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0812× (z -9.7) |
| [[SW480 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 9 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APRT]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[C20orf27]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MRPL12]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NPM3]] | +0.67 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[NAA10]] ⚠ | +0.67 | +0.59 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MICOS13]] | +0.65 | +0.48 / +0.63 | both halves | 2e-05 | STRING 452 |
| [[NHP2]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 | STRING 449 |
| [[MRPL41]] ⚠ | +0.64 | +0.50 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AURKAIP1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TOMM22]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 | pathway: Protein localization |
| [[DCTPP1]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MRPS12]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PUSL1]] | +0.59 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[ANTKMT]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD3]] | -0.59 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PAN2]] | -0.55 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[RYR2]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[MALINC1]] | -0.52 | -0.49 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[CROCC]] | -0.52 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[DHX38]] | -0.51 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[HNRNPH1]] | -0.51 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[ITFG2-AS1]] | -0.51 | -0.44 / -0.26 | both halves | 3e-04 |  |
| [[SRSF5]] | -0.51 | -0.24 / -0.47 | both halves | 5e-04 |  |
| [[AGER]] | -0.50 | -0.49 / -0.21 | both halves | 7e-04 |  |
| [[COL11A2]] | -0.49 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[STXBP2]] | -0.49 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[CLK1]] | -0.49 | -0.56 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.5, -15.1); signed map (-37.6, -27.6). **Vector** length 49.8, 10.6% of its response variance represented; |z| ≥ 3 in 487 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.59 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +2.5 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -1.5 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.0 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 147 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,545,600-35,547,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NIFIE14, MGC1936 |
| Gene groups (HGNC) | BOS complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVK8](https://www.uniprot.org/uniprotkb/Q9BVK8) (BOS complex subunit TMEM147):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions. Also acts as a negative regulator of CHRM3 function, most likely by …

**Summary**, from NCBI Gene [10430](https://www.ncbi.nlm.nih.gov/gene/10430):

> Enables ribosome binding activity. Involved in multi-pass transmembrane protein insertion into ER membrane and protein localization to nuclear inner membrane. Located in nuclear membrane. Part of multi-pass translocon complex. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30414) · Entrez [10430](https://www.ncbi.nlm.nih.gov/gene/10430) · UniProt [Q9BVK8](https://www.uniprot.org/uniprotkb/Q9BVK8) · Ensembl [ENSG00000105677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105677)

## Data

Gene col 2644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2644); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2644]; `tensor/DDL_lfc|DDL_z.npy` [2644]; `embed/gene_vectors.npy` [2644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2644 or target_col == 2644). Every well: [[TMEM147 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM147.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
