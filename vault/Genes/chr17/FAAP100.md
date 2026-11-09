---
symbol: "FAAP100"
type: "gene"
col: 11689
ensembl_id: "ENSG00000185504"
name: "FA core complex associated protein 100"
location: "17q25.3"
module: 2
arm: "+"
pooled_cpm: 4.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FAAP100

*FA core complex associated protein 100* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +9.2, q 2e-17, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.96× (z +7.7, q 4e-12, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.697× (z -5.9, q 2e-06, down in 16 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFRP1]] (+0.80, fdr 7e-06), [[ARHGDIA]] (+0.72, fdr 7e-06), [[NCDN]] (+0.71, fdr 7e-06); moves opposite to [[ARL6IP5]] (-0.57, fdr 1e-05), [[NSD3]] (-0.54, fdr 2e-05), [[TMEM59]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DAGLA]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.2 | 2e-17 | 6/9 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +7.7 | 4e-12 | 29/47 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +6.2 | 9e-08 | 20/39 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.9 | 7e-07 | 8/23 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 3e-05 | 14/45 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.0 | 5e-05 | 7/46 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +4.9 | 9e-05 | 15/44 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 9e-05 | 17/39 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 13/44 (PANC-1, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.6 | 2e-04 | 5/11 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.0 | 0.003 | 8/45 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.9 | 0.005 | 5/27 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.069 | 2/26 (HS-578T, A-172) | top dose only | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.084 | 2/44 (A-427, H4) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -5.9 | 2e-06 | 16/40 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.021 | 12/43 (A498, NCI-H2030, …) | top dose only |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **0.719×** | -3.8 | 0.028 | 12/44 (HOP62, RKO, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.037 | 11/42 (RKO, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.054 | 7/39 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vandetanib (drug)]] 5 µM |  | 0.761× | -3.2 | 0.15 | 11/46 (BT-474, HT-29, …) | inconsistent across doses | position effect removed |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.18 | 2/44 (PANC-1, BT-474) | inconsistent across doses | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | 0.771× | -3.0 | 0.19 | 5/38 (CFPAC-1, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 6.81 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0834× (z -10.3) |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.126× (z -9.6) |
| [[HS-578T (line)]] | alt | 4.63 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0671× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 3.15 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.108× (z -8.7) |
| [[SNU-423 (line)]] | alt | 5.65 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0663× (z -9.8) |
| [[A-172 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFRP1]] | +0.80 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ARHGDIA]] | +0.72 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NCDN]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TRMT61A]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[THOP1]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZYX]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[RNF123]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[APEH]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PLEKHG4]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.63 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[CEP170B]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6IP5]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NSD3]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TMEM59]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[HOXB4]] | -0.53 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[TNFSF13B]] | -0.53 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[SOS1]] | -0.53 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[LINC02680]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[HOXA5]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[LEPR]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAGLA]] | C | DAGLA activity raises FAAP100's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without DAGLA | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.3, -25.5); signed map (-7.1, 30.4). **Vector** length 55.6, 7.00% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FA core complex associated protein 100 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,539,885-81,553,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22175; previously C17orf70 |
| Gene groups (HGNC) | FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VG06](https://www.uniprot.org/uniprotkb/Q0VG06) (Fanconi anemia core complex-associated protein 100):

> Plays a role in Fanconi anemia-associated DNA damage response network. Regulates FANCD2 monoubiquitination and the stability of the FA core complex. Induces chromosomal instability as well as hypersensitivity to DNA cross-linking agents, when repressed.

**Summary**, from NCBI Gene [80233](https://www.ncbi.nlm.nih.gov/gene/80233):

> FAAP100 is a component of the Fanconi anemia (FA; MIM 277650) core complex and is required for core complex stability and FANCD2 (see MIM 227646) monoubiquitination (Ling et al., 2007 [PubMed 17396147]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26171) · Entrez [80233](https://www.ncbi.nlm.nih.gov/gene/80233) · UniProt [Q0VG06](https://www.uniprot.org/uniprotkb/Q0VG06) · Ensembl [ENSG00000185504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185504)

## Data

Gene col 11689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11689); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11689]; `tensor/DDL_lfc|DDL_z.npy` [11689]; `embed/gene_vectors.npy` [11689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11689 or target_col == 11689). Every well: [[FAAP100 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAAP100.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
