---
symbol: "FARSA"
type: "gene"
col: 11001
ensembl_id: "ENSG00000179115"
name: "phenylalanyl-tRNA synthetase subunit alpha"
location: "19p13.13"
module: 33
arm: "+"
pooled_cpm: 12.91
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FARSA

*phenylalanyl-tRNA synthetase subunit alpha* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.68× (z +8.5, q 1e-14, up in 34 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.54× (z +7.1, q 4e-10, up in 24 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.176×, NCI-H23 0.321×, MIA PaCa-2 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0939×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (HCT15 0.0763×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0817×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW1417 0.208×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLE1]] (+0.69, fdr 7e-06), [[POLR1B]] (+0.67, fdr 7e-06), [[SCO1]] (+0.65, fdr 7e-06); moves opposite to [[TAX1BP1]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +8.5 | 1e-14 | 34/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.1 | 4e-10 | 24/46 (Hs 766T, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +6.9 | 1e-09 | 23/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 5e-07 | 22/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.7 | 1e-06 | 21/47 (SNU-423, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +5.5 | 3e-06 | 20/47 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.83×** | +5.1 | 2e-05 | 13/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 5e-05 | 18/42 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +4.4 | 6e-04 | 10/45 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +4.3 | 9e-04 | 10/45 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.006 | 7/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.8 | 0.006 | 9/48 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.011 | 13/48 (A-172, J82, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.016 | 13/44 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.028 | 7/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.034 | 11/46 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.034 | 4/47 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.0 | 0.068 | 5/48 (CFPAC-1, H4, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.090 | 7/46 (Hs 766T, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.176×, NCI-H23 0.321×, MIA PaCa-2 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0939×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (HCT15 0.0763×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0817×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW1417 0.208×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.1 | 0.97 | 19/46 (A-427, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 21.3 | 0 | 2 | — | [[Bergenin (drug)]] 0.5 µM 0.0763× (z -12.8) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.163× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 9.32 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0854× (z -9.2) |
| [[KATO III (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0939× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.208× (z -9.3) |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLE1]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SCO1]] | +0.65 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[RFT1]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.64 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[DDX55]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[MRPS23]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[WDR3]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[COA4]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAX1BP1]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.2, -40.2); signed map (-7.1, -51.8). **Vector** length 67.3, 10.7% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +5.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~7% of this change | +2.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | phenylalanyl-tRNA synthetase subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,922,479-12,934,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CML33; previously FARSL, FARSLA |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y285](https://www.uniprot.org/uniprotkb/Q9Y285) (Phenylalanine--tRNA ligase alpha subunit):

> Catalytic alpha subunit of cytoplasmic phenylalanyl-tRNA synthetase, an enzyme that catalyzes the esterification of phenylalanine to its cognate tRNA with the concomitant hydrolysis of ATP. The activated amino acid is transferred to the 2-OH group of a phenylalanine-accepting tRNA.

**Summary**, from NCBI Gene [2193](https://www.ncbi.nlm.nih.gov/gene/2193):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. This gene encodes a product which is similar to the catalytic subunit of prokaryotic and Saccharomyces cerevisiae phenylalanyl-tRNA synthetases (PheRS). This gene product has been shown to be expressed in a tumor-selective and cell cycle stage- and differentiation-dependent manner, the first member of the tRNA synthetase gene family shown to exhibit this type of regulated expression [provided by …

**Accessions** — [HGNC:3592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3592) · Entrez [2193](https://www.ncbi.nlm.nih.gov/gene/2193) · UniProt [Q9Y285](https://www.uniprot.org/uniprotkb/Q9Y285) · Ensembl [ENSG00000179115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179115)

## Data

Gene col 11001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11001); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11001]; `tensor/DDL_lfc|DDL_z.npy` [11001]; `embed/gene_vectors.npy` [11001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11001 or target_col == 11001). Every well: [[FARSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FARSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
