---
symbol: "MRPL23"
type: "gene"
col: 13164
ensembl_id: "ENSG00000214026"
name: "mitochondrial ribosomal protein L23"
location: "11p15.5"
module: 24
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MRPL23

*mitochondrial ribosomal protein L23* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +6.0, q 1e-06, up in 23 of 26 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.413× (z -6.4, q 1e-07, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.71, fdr 2e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SELENOH]] (+0.71, fdr 1e-05), [[MINCR]] (+0.70, fdr 7e-06), [[ATP5MC2]] (+0.69, fdr 8e-06); moves opposite to [[MAPRE1]] (-0.69, fdr 1e-05), [[MOB1A]] (-0.67, fdr 1e-05), [[LIN7C]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +6.0 | 1e-06 | 23/26 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +5.8 | 2e-06 | 6/9 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.6 | 0.042 | 16/42 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.042 | 17/42 (PANC-1, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | 1.56× | +3.2 | 0.17 | 10/29 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Erythromycin (drug)]] 5 µM |  | 1.53× | +3.1 | 0.21 | 7/45 (LoVo, H4, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.413×** | -6.4 | 1e-07 | 31/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.624×** | -4.8 | 4e-04 | 23/39 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.539×** | -4.5 | 0.001 | 23/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.650×** | -4.4 | 0.001 | 17/45 (SW480, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -4.4 | 0.001 | 23/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.525×** | -4.4 | 0.001 | 21/43 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.580×** | -3.9 | 0.007 | 22/46 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.693×** | -3.7 | 0.014 | 19/45 (NCI-H460, PANC-1, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -3.7 | 0.015 | 15/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -3.4 | 0.042 | 10/44 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.605×** | -3.3 | 0.043 | 8/47 (NCI-H1573, C-33 A, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.638×** | -3.2 | 0.058 | 18/43 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.620×** | -3.2 | 0.060 | 9/45 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.732×** | -3.2 | 0.060 | 17/40 (RPMI-7951, SW480, …) | top dose only | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.622×** | -3.2 | 0.060 | 5/44 (PANC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.653×** | -3.1 | 0.076 | 10/48 (CHP-212, SW480, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.636×** | -3.0 | 0.088 | 6/45 (A498, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.26 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0822× (z -8.5) |
| [[J82 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.1) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.7) |
| [[A-172 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 12 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.71 | +0.48 / +0.74 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | +0.71 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[MINCR]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.69 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[TMEM258]] | +0.68 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[NSUN5P2-1]] ⚠ | +0.67 | +0.45 / +0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD5]] | +0.67 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[SNHG9]] | +0.66 | +0.43 / +0.71 | both halves | 4e-05 |  |
| [[TRIM52-AS1]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[WDR83OS]] ⚠ | +0.66 | +0.47 / +0.72 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 915 |
| [[NACA4P]] ⚠ | +0.65 | +0.39 / +0.70 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.65 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[ACAD10]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MRPS18C]] | +0.64 | +0.40 / +0.66 | both halves | 4e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 986 |
| [[SNHG19]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.69 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.67 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.65 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.65 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.64 | -0.36 / -0.72 | both halves | 1e-04 |  |
| [[TWF1]] | -0.64 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[FLNA]] | -0.61 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[YWHAQ]] | -0.60 | -0.38 / -0.72 | both halves | 7e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[DCTN1]] | -0.59 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[CDC42]] | -0.59 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[PGRMC1]] | -0.59 | -0.41 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -21.3); signed map (-30.2, 6.8). **Vector** length 46.6, 6.77% of its response variance represented; |z| ≥ 3 in 614 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.4 | -4.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.4 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,947,278-1,984,522 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L23MRP, uL23m; previously RPL23L |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | UV_RESPONSE_UP, MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q16540](https://www.uniprot.org/uniprotkb/Q16540) carries no function annotation.

**Summary**, from NCBI Gene [6150](https://www.ncbi.nlm.nih.gov/gene/6150):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:10322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10322) · Entrez [6150](https://www.ncbi.nlm.nih.gov/gene/6150) · UniProt [Q16540](https://www.uniprot.org/uniprotkb/Q16540) · Ensembl [ENSG00000214026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214026)

## Data

Gene col 13164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13164); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13164]; `tensor/DDL_lfc|DDL_z.npy` [13164]; `embed/gene_vectors.npy` [13164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13164 or target_col == 13164). Every well: [[MRPL23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
