---
symbol: "SEC16A"
type: "gene"
col: 7277
ensembl_id: "ENSG00000148396"
name: "SEC16 homolog A, endoplasmic reticulum export factor"
location: "9q34.3"
module: 52
arm: "+"
pooled_cpm: 105.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SEC16A

*SEC16 homolog A, endoplasmic reticulum export factor* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +5.9, q 3e-06, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.698× (z -7.4, q 4e-11, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.70, fdr 7e-06), [[GOSR2]] (+0.69, fdr 7e-06), [[COPE]] (+0.68, fdr 7e-06); moves opposite to [[ZNF326]] (-0.66, fdr 1e-05), [[PAIP1]] (-0.57, fdr 1e-05), [[WDSUB1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +5.9 | 3e-06 | 38/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.1 | 1e-04 | 34/49 (COLO 205, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.008 | 33/48 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.4 | 0.087 | 26/48 (SW1417, SNU-423, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.3 | 0.087 | 26/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.087 | 14/49 (COLO 205, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.087 | 24/48 (SNU-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.12 | 22/48 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.698×** | -7.4 | 4e-11 | 42/48 (SNU-423, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -7.4 | 4e-11 | 38/49 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.585×** | -7.2 | 8e-11 | 32/45 (SHP-77, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -6.3 | 5e-08 | 29/44 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.703×** | -5.2 | 3e-05 | 39/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.740×** | -4.4 | 0.001 | 35/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.005 | 27/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.053 | 20/48 (A549, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.053 | 23/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.3 | 0.054 | 18/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.086 | 22/48 (A549, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -19.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.460× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 82.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 94.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 98.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.147× (z -9.1) ⚠ cell-cycle shift, explains ~2% of this change |
| [[Panc 03.27 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -15.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 155 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0738× (z -13.5) |
| [[SW480 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 148 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOSR2]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 642 |
| [[COPE]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 466 |
| [[GOLGA3]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RER1]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[DMPK]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PMM2]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[POFUT2]] | +0.64 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[P4HB]] | +0.64 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[HM13]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF326]] | -0.66 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[WDSUB1]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[VRK2]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[HDAC2]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MAP4K5]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HSF2]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MIER1]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PLEKHF2]] | -0.52 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SSB]] | -0.52 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.6, -28.6); signed map (-51.0, 4.5). **Vector** length 127, 41.8% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.4 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | -6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +0.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.8 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.5 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SEC16 homolog A, endoplasmic reticulum export factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,440,096-136,483,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p250, Sec16L; previously KIAA0310 |
| Gene groups (HGNC) | SEC16 endoplasmic reticulum export factor family |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [O15027](https://www.uniprot.org/uniprotkb/O15027) (Protein transport protein Sec16A):

> Acts as a molecular scaffold that plays a key role in the organization of the endoplasmic reticulum exit sites (ERES), also known as transitional endoplasmic reticulum (tER). SAR1A-GTP-dependent assembly of SEC16A on the ER membrane forms an organized scaffold defining an ERES. Required for secretory cargo traffic from the endoplasmic reticulum to the Golgi apparatus. Mediates the recruitment of MIA3/TANGO to ERES. Regulates both conventional (ER/Golgi-dependent) and GORASP2-mediated …

**Summary**, from NCBI Gene [9919](https://www.ncbi.nlm.nih.gov/gene/9919):

> This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:29006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29006) · Entrez [9919](https://www.ncbi.nlm.nih.gov/gene/9919) · UniProt [O15027](https://www.uniprot.org/uniprotkb/O15027) · Ensembl [ENSG00000148396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148396)

## Data

Gene col 7277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7277); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7277]; `tensor/DDL_lfc|DDL_z.npy` [7277]; `embed/gene_vectors.npy` [7277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7277 or target_col == 7277). Every well: [[SEC16A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC16A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
