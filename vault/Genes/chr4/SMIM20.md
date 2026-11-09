---
symbol: "SMIM20"
type: "gene"
col: 14684
ensembl_id: "ENSG00000250317"
name: "small integral membrane protein 20"
location: "4p15.2"
module: 63
arm: "+"
pooled_cpm: 11.13
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SMIM20

*small integral membrane protein 20* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +9.8, q 4e-20, up in 30 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +4.7, q 4e-04, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 5.08×, LS 180 4.42×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.47×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -8.3, q 8e-14, down in 31 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.170×, LoVo 0.276×, NCI-H460 0.303×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0811×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (C32 0.107×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLGN]] (+0.55, fdr 3e-05), [[PFDN4]] (+0.55, fdr 1e-05), [[HECW1]] (+0.54, fdr 2e-05); moves opposite to [[CFL1]] (-0.48, fdr 3e-05), [[SRSF2]] (-0.48, fdr 1e-04), [[DNMT1]] (-0.47, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 5.08×, LS 180 4.42×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.47×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.8 | 4e-20 | 30/34 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.4 | 5e-11 | 17/24 (SW 900, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +5.5 | 6e-06 | 25/41 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.7 | 4e-04 | 24/46 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.1 | 0.005 | 17/27 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.026 | 15/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.16 | 12/46 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.1 | 0.16 | 16/44 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.170×, LoVo 0.276×, NCI-H460 0.303×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0811×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (C32 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -8.3 | 8e-14 | 31/44 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.745× | -3.3 | 0.23 | 12/46 (AsPC-1, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.767× | -3.0 | 0.47 | 14/46 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.9) |
| [[LoVo (line)]] | wt | 15.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.08× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.5) |
| [[C32 (line)]] | wt | 9.33 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.107× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 9.48 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0811× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 7.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.42× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.9) |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0993× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLGN]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PFDN4]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[HECW1]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SEPHS2]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ZFAND1]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TOM1L1]] | +0.52 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[DMAC2]] | +0.50 | +0.56 / +0.29 | both halves | 2e-04 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[PIR]] | +0.50 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[FTL]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ZNF32]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[POPDC3]] | +0.49 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[RPL39]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SRSF2]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[DNMT1]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[NAB1]] | -0.46 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[WDR90]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MYLK2]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[STMN3]] | -0.45 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[CTSE]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[MYEOV]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[HIVEP3]] | -0.44 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[ITGB4]] | -0.43 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.43 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.5, 50.5); signed map (-25.1, -22.1). **Vector** length 46.9, 6.34% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,861,830-25,929,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PNX, MITRAC7; previously C4orf52 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5G0](https://www.uniprot.org/uniprotkb/Q8N5G0) (Small integral membrane protein 20):

> [Small integral membrane protein 20]: Component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly. Promotes the progression of complex assembly after the association of MT-CO1/COX1 with COX4I1 and COX6C. Chaperone-like assembly factor required to stabilize newly synthesized MT-CO1/COX1 and to prevent its premature turnover.; [Phoenixin-14]: Peptide involved in a broad spectrum of …

**Summary**, from NCBI Gene [389203](https://www.ncbi.nlm.nih.gov/gene/389203):

> Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37260) · Entrez [389203](https://www.ncbi.nlm.nih.gov/gene/389203) · UniProt [Q8N5G0](https://www.uniprot.org/uniprotkb/Q8N5G0) · Ensembl [ENSG00000250317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250317)

## Data

Gene col 14684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14684); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14684]; `tensor/DDL_lfc|DDL_z.npy` [14684]; `embed/gene_vectors.npy` [14684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14684 or target_col == 14684). Every well: [[SMIM20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
