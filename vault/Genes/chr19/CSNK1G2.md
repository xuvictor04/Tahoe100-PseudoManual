---
symbol: "CSNK1G2"
type: "gene"
col: 5436
ensembl_id: "ENSG00000133275"
name: "casein kinase 1 gamma 2"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 45.96
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CSNK1G2

*casein kinase 1 gamma 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +5.4, q 4e-05, up in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +4.0, q 0.010, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.488× (z -11.2, q 2e-26, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD13D]] (+0.76, fdr 7e-06), [[FOXK2]] (+0.73, fdr 7e-06), [[PITPNA]] (+0.73, fdr 7e-06); moves opposite to [[MBTPS2]] (-0.69, fdr 1e-05), [[HUS1]] (-0.68, fdr 7e-06), [[NBN]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.4 | 4e-05 | 36/48 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.6 | 0.001 | 28/43 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.010 | 29/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.041 | 34/48 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.078 | 25/48 (A-172, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.33×** | +3.3 | 0.078 | 27/48 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.078 | 28/47 (NCI-H23, HepG2/C3A, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.58× | +3.0 | 0.15 | 24/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.57× | +3.0 | 0.15 | 22/48 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -11.2 | 2e-26 | 41/48 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -8.5 | 5e-15 | 41/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.648×** | -4.8 | 3e-04 | 35/48 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -4.6 | 6e-04 | 4/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -4.5 | 1e-03 | 34/48 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -3.8 | 0.013 | 30/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.812× | -3.2 | 0.10 | 23/48 (SK-MEL-2, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.13 | 23/48 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.750× | -3.0 | 0.16 | 19/48 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 53.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -20.7) |
| [[A-172 (line)]] | wt | 72.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.4) |
| [[C32 (line)]] | wt | 43.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -12.4) |
| [[HS-578T (line)]] | alt | 58.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 67.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.8) |
| [[A498 (line)]] | wt | 57.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.7) |
| [[COLO 205 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.1) |
| [[HT-29 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.9) |
| [[J82 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.5) |
| [[LoVo (line)]] | wt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.8) |
| [[RKO (line)]] | wt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -8.7) |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.5) |
| [[SW480 (line)]] | alt | 49.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.6) |
| [[A549 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13D]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[PITPNA]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MARK4]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[NFATC2IP-AS1]] | +0.68 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[AGAP3]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[DRD4]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CASTOR3P]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SRGAP2D]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBTPS2]] | -0.69 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[HUS1]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[NBN]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.66 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[GMFB]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[TAF9]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ZXDA]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[CFL2]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.61 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[ZNF678]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.9, -3.9); signed map (-42.3, 1.3). **Vector** length 90.5, 26.7% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | -0.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,941,172-1,981,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CK1g2 |
| Gene groups (HGNC) | Casein kinase 1 family |
| Reactome | 6 pathways, smallest: Disassembly of the destruction complex and recruitment of AXIN to the membrane; Sphingolipid de novo biosynthesis; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P78368](https://www.uniprot.org/uniprotkb/P78368) (Casein kinase I isoform gamma-2):

> Serine/threonine-protein kinase. Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. It can phosphorylate a large number of proteins. Participates in Wnt signaling (By similarity). Phosphorylates COL4A3BP/CERT, MTA1 and SMAD3. SMAD3 phosphorylation promotes its ligand-dependent ubiquitination and subsequent proteasome degradation, thus inhibiting SMAD3-mediated TGF-beta responses. Hyperphosphorylation of the serine-repeat …

**Summary**, from NCBI Gene [1455](https://www.ncbi.nlm.nih.gov/gene/1455):

> Enables protein serine/threonine kinase activity. Predicted to be involved in endocytosis; positive regulation of canonical Wnt signaling pathway; and signal transduction. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2455) · Entrez [1455](https://www.ncbi.nlm.nih.gov/gene/1455) · UniProt [P78368](https://www.uniprot.org/uniprotkb/P78368) · Ensembl [ENSG00000133275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133275)

## Data

Gene col 5436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5436); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5436]; `tensor/DDL_lfc|DDL_z.npy` [5436]; `embed/gene_vectors.npy` [5436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5436 or target_col == 5436). Every well: [[CSNK1G2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1G2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
