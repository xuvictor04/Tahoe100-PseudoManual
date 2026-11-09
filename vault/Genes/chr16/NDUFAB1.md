---
symbol: "NDUFAB1"
type: "gene"
col: 53
ensembl_id: "ENSG00000004779"
name: "NADH:ubiquinone oxidoreductase subunit AB1"
location: "16p12.2"
module: 58
arm: "+"
pooled_cpm: 24.74
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

# NDUFAB1

*NADH:ubiquinone oxidoreductase subunit AB1* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +7.1, q 6e-10, up in 40 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.35× (z +3.9, q 0.011, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.687× (z -3.9, q 0.047, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.163×, AsPC-1 0.278×); [[Entrectinib (drug)]] 5 µM in 1 line (CHP-212 0.0477×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT112]] (+0.80, fdr 7e-06), [[NDUFS8]] (+0.73, fdr 7e-06), [[NDUFA3]] (+0.71, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.57, fdr 4e-05), [[EIF4G2]] (-0.56, fdr 4e-05), [[HLA-H]] (-0.55, fdr 2e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 53.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.78×** | +7.1 | 6e-10 | 40/42 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.27×** | +5.8 | 2e-06 | 29/35 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.03×** | +4.2 | 0.004 | 31/39 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.2 | 0.005 | 33/46 (NCI-H1573, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.35×** | +3.9 | 0.011 | 41/47 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.64×** | +3.7 | 0.020 | 32/46 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.22×** | +3.7 | 0.020 | 38/47 (MIA PaCa-2, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.020 | 28/48 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +3.3 | 0.063 | 31/44 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.56×** | +3.3 | 0.063 | 27/46 (A-172, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.94× | +3.0 | 0.11 | 25/47 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.94× | +3.0 | 0.11 | 30/46 (HCT15, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 53.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.163×, AsPC-1 0.278×); [[Entrectinib (drug)]] 5 µM in 1 line (CHP-212 0.0477×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.047 | 29/47 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.742× | -3.1 | 0.50 | 24/48 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 53. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.4) |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0477× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 53), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT112]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NDUFS8]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFA3]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFS5]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[DPY30]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[BMS1P4]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[NDUFB3]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[DHX57]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CENPX]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[NDUFS7]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFB7]] | +0.63 | +0.49 / +0.70 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.57 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.56 | -0.41 / -0.48 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HLA-H]] | -0.55 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[THAP9]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.53 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[MYOSLID]] | -0.53 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[YWHAZ]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[TUG1]] | -0.52 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HMGN2]] | -0.51 | -0.44 / -0.39 | both halves | 6e-05 | STRING 626 |
| [[HMGN1]] | -0.51 | -0.56 / -0.38 | both halves | 7e-05 | STRING 634 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.5, -19.0); signed map (-37.4, 6.8). **Vector** length 71.8, 21.2% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.2 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -3.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.6 | +7.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit AB1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,581,014-23,596,316 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mtACP, mt-ACP, SDAP, FASN2A, ACP, ACP1 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | ADIPOGENESIS, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Protein lipoylation; Mitochondrial Fatty Acid Beta-Oxidation; Complex I biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O14561](https://www.uniprot.org/uniprotkb/O14561) (Acyl carrier protein, mitochondrial):

> Carrier of the growing fatty acid chain in fatty acid biosynthesis (By similarity). Accessory and non-catalytic subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), which functions in the transfer of electrons from NADH to the respiratory chain. Accessory protein, of the core iron-sulfur cluster (ISC) assembly complex, that regulates, in association with LYRM4, the stability and the cysteine desulfurase activity of NFS1 and participates in the [2Fe-2S] …

**Summary**, from NCBI Gene [4706](https://www.ncbi.nlm.nih.gov/gene/4706):

> Enables mitochondrial large ribosomal subunit binding activity and structural molecule activity. Involved in [2Fe-2S] cluster assembly; mitochondrial large ribosomal subunit assembly; and protein lipoylation. Located in mitochondrial inner membrane. Part of mitochondrial [2Fe-2S] assembly complex and respiratory chain complex I. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7694) · Entrez [4706](https://www.ncbi.nlm.nih.gov/gene/4706) · UniProt [O14561](https://www.uniprot.org/uniprotkb/O14561) · Ensembl [ENSG00000004779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004779)

## Data

Gene col 53: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 53); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 53, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 53]; `tensor/DDL_lfc|DDL_z.npy` [53]; `embed/gene_vectors.npy` [53]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 53 or target_col == 53). Every well: [[NDUFAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
