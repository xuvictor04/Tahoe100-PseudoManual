---
symbol: "RNF26"
type: "gene"
col: 10387
ensembl_id: "ENSG00000173456"
name: "ring finger protein 26"
location: "11q23.3"
module: 22
arm: "+"
pooled_cpm: 7.66
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# RNF26

*ring finger protein 26* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.05× (z +7.5, q 5e-11, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.520× (z -6.8, q 6e-09, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNA2]] (+0.75, fdr 7e-06), [[PLK1]] (+0.73, fdr 7e-06), [[KIF20A]] (+0.73, fdr 7e-06); moves opposite to [[EOGT-DT]] (-0.58, fdr 4e-05), [[ZRANB2-AS1]] (-0.53, fdr 5e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +7.5 | 5e-11 | 35/47 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.77×** | +5.8 | 2e-06 | 24/38 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +5.6 | 4e-06 | 11/22 (SW1417, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.5 | 7e-06 | 23/47 (Hs 766T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.8 | 2e-04 | 21/47 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 16/47 (RPMI-7951, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +4.0 | 0.004 | 11/48 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +3.4 | 0.042 | 6/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.066 | 7/47 (NCI-H1573, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.37×** | +3.2 | 0.066 | 4/47 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.53×** | +3.1 | 0.089 | 9/28 (HOP62, A-427, …) | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.520×** | -6.8 | 6e-09 | 29/47 (SW480, LoVo, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.007 | 18/47 (HS-578T, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -4.1 | 0.007 | 18/44 (SNU-423, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -3.8 | 0.017 | 14/44 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.025 | 17/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.730× | -3.1 | 0.17 | 9/47 (CHP-212, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.812× | -3.1 | 0.17 | 10/47 (RPMI-7951, SNU-1, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.749× | -3.0 | 0.19 | 11/47 (AN3 CA, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0318× (z -12.9) |
| [[SNU-423 (line)]] | alt | 7.38 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0636× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 5 µM 0.0918× (z -9.9) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.150× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 4.79 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0647× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0864× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNA2]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PLK1]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[CCNB1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PSRC1]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[BUB1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[INCENP]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CCNB2]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[KNSTRN]] | +0.67 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CKAP5]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CCNF]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ARHGAP11A]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT-DT]] | -0.58 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises RNF26's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without NEURL1B | 0.073 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[CDCA3]] | C | CDCA3 activity raises RNF26's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -57.9); signed map (-51.8, -43.3). **Vector** length 72.8, 13.0% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.53 to 60); *DREAM G2/M down* (control, mean cos +0.59 to 28); *E2F targets* (hallmark, mean cos +0.50 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | +4.9 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,334,527-119,337,309 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2642 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY78](https://www.uniprot.org/uniprotkb/Q9BY78) (E3 ubiquitin-protein ligase RNF26):

> E3 ubiquitin-protein ligase that plays a key role in endosome organization by retaining vesicles in the perinuclear cloud. Acts as a platform for perinuclear positioning of the endosomal system by mediating ubiquitination of SQSTM1 through interaction with the ubiquitin conjugating enzyme UBE2J1. Ubiquitinated SQSTM1 attracts specific vesicle-associated adapters, forming a molecular bridge that restrains cognate vesicles in the perinuclear region and organizes the endosomal pathway for …

**Summary**, from NCBI Gene [79102](https://www.ncbi.nlm.nih.gov/gene/79102):

> The protein encoded by this intronless gene contains a C3HC5 type of RING finger, a motif known to be involved in protein-DNA and protein-protein interactions. The expression of this gene was found to be upregulated in cancer cell lines derived from different types of cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14646) · Entrez [79102](https://www.ncbi.nlm.nih.gov/gene/79102) · UniProt [Q9BY78](https://www.uniprot.org/uniprotkb/Q9BY78) · Ensembl [ENSG00000173456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173456)

## Data

Gene col 10387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10387); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10387]; `tensor/DDL_lfc|DDL_z.npy` [10387]; `embed/gene_vectors.npy` [10387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10387 or target_col == 10387). Every well: [[RNF26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
