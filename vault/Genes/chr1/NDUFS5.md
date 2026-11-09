---
symbol: "NDUFS5"
type: "gene"
col: 9679
ensembl_id: "ENSG00000168653"
name: "NADH:ubiquinone oxidoreductase subunit S5"
location: "1p34.3"
module: 58
arm: "+"
pooled_cpm: 48.74
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFS5

*NADH:ubiquinone oxidoreductase subunit S5* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +9.4, q 5e-18, up in 45 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.58× (z +4.0, q 0.005, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.678× (z -4.7, q 0.001, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.364×, RKO 0.375×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf53]] (+0.71, fdr 7e-06), [[SNRPD2]] (+0.70, fdr 1e-05), [[UQCR11]] (+0.70, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.59, fdr 2e-04), [[C19orf54]] (-0.53, fdr 7e-04), [[PPP1R15A]] (-0.52, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.12×** | +9.4 | 5e-18 | 45/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.79×** | +8.6 | 3e-15 | 38/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.8 | 1e-06 | 41/45 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.09×** | +5.3 | 2e-05 | 37/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.79×** | +5.1 | 4e-05 | 41/47 (PANC-1, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.73×** | +4.8 | 2e-04 | 39/47 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.005 | 35/48 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.074 | 32/48 (HOP62, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.00×** | +3.2 | 0.078 | 33/48 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.56×** | +3.2 | 0.079 | 30/48 (NCI-H460, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9679.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.364×, RKO 0.375×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -4.7 | 0.001 | 35/48 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.672× | -3.4 | 0.18 | 29/48 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 56.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 55.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 33.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.8) |
| [[RKO (line)]] | wt | 75.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.6) |
| [[SW 900 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf53]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SNRPD2]] | +0.70 | +0.74 / +0.57 | both halves | 1e-05 | STRING 586 |
| [[UQCR11]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 986 |
| [[NDUFB7]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[NDUFAB1]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[NDUFS8]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[NDUFA3]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[COX6C]] | +0.65 | +0.68 / +0.51 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 959 |
| [[DPY30]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ELOB]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NDUFB3]] | +0.62 | +0.46 / +0.64 | both halves | 2e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[UQCRQ]] ⚠ | +0.62 | +0.56 / +0.54 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 993; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC2]] | +0.61 | +0.43 / +0.65 | both halves | 3e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.59 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[C19orf54]] | -0.53 | -0.58 / -0.20 | both halves | 7e-04 |  |
| [[PPP1R15A]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GALNT7-DT]] | -0.51 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[SGO1-AS1]] | -0.50 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[PKN2-AS1]] | -0.50 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[PDCL3P4]] | -0.50 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[THAP2]] | -0.50 | -0.54 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[MAILR]] | -0.49 | -0.47 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[PCNX4-DT]] | -0.49 | -0.47 / -0.20 | both halves | 7e-04 |  |
| [[PAN2]] | -0.49 | -0.45 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.3, -19.5); signed map (-37.4, 6.9). **Vector** length 61.3, 18.0% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit S5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:39,026,318-39,034,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-15k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43920](https://www.uniprot.org/uniprotkb/O43920) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4725](https://www.ncbi.nlm.nih.gov/gene/4725):

> This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:7712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7712) · Entrez [4725](https://www.ncbi.nlm.nih.gov/gene/4725) · UniProt [O43920](https://www.uniprot.org/uniprotkb/O43920) · Ensembl [ENSG00000168653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168653)

## Data

Gene col 9679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9679); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9679]; `tensor/DDL_lfc|DDL_z.npy` [9679]; `embed/gene_vectors.npy` [9679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9679 or target_col == 9679). Every well: [[NDUFS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
