---
symbol: "CLPP"
type: "gene"
col: 4640
ensembl_id: "ENSG00000125656"
name: "caseinolytic mitochondrial matrix peptidase proteolytic subunit"
location: "19p13.3"
module: 54
arm: "+"
pooled_cpm: 10.67
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CLPP

*caseinolytic mitochondrial matrix peptidase proteolytic subunit* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +5.7, q 7e-06, up in 15 of 19 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -8.5, q 2e-14, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.66, fdr 1e-05), [[GID4]] (+0.64, fdr 7e-06), [[MRPS12]] (+0.64, fdr 2e-04); moves opposite to [[WDR1]] (-0.58, fdr 1e-04), [[MYH9]] (-0.56, fdr 2e-04), [[SFPQ]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.7 | 7e-06 | 15/19 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.77×** | +5.5 | 1e-05 | 26/42 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.90×** | +5.2 | 4e-05 | 25/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.004 | 22/41 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.28× | +3.3 | 0.11 | 9/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.39× | +3.2 | 0.15 | 17/47 (SNU-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -8.5 | 2e-14 | 35/47 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -6.0 | 7e-07 | 32/43 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.549×** | -5.7 | 2e-06 | 33/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.618×** | -4.6 | 7e-04 | 24/47 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.629×** | -4.4 | 0.001 | 26/47 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -4.4 | 0.001 | 23/47 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.019 | 22/48 (RKO, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.073 | 21/46 (RPMI-7951, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.6) |
| [[Hs 766T (line)]] | wt | 9.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.9) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 9.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.4) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0833× (z -9.0) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[GID4]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MRPS12]] | +0.64 | +0.31 / +0.72 | both halves | 2e-04 | STRING 537 |
| [[GAPVD1]] | +0.63 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.63 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[ASB7]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[POP7]] | +0.62 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[MRPL34]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NENF]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 | STRING 451; ⚠ same locus (2.6 kb, same strand: neighbours can correlate without regulation) |
| [[FHIP2A]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LAMTOR2]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MFSD5]] | +0.60 | +0.45 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | -0.58 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[MYH9]] | -0.56 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[SFPQ]] | -0.53 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[SUB1]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NAB1]] | -0.53 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.53 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[CHMP4B]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MMRN2]] | -0.53 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[IER2]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[COL16A1]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[JUNB]] | -0.52 | -0.24 / -0.60 | both halves | 4e-04 |  |
| [[LINC00641]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CLPP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CLPP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.5, -9.4); signed map (-39.4, 2.9). **Vector** length 48.0, 7.46% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | caseinolytic mitochondrial matrix peptidase proteolytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,361,531-6,370,242 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 1 pathways, smallest: Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16740](https://www.uniprot.org/uniprotkb/Q16740) (ATP-dependent Clp protease proteolytic subunit, mitochondrial):

> Protease component of the ClpXP complex that cleaves peptides and various proteins in an ATP-dependent process. Has low peptidase activity in the absence of CLPX. The ClpXP complex can degrade CSN1S1, CSN2 and CSN3, as well as synthetic peptides (in vitro) and may be responsible for a fairly general and central housekeeping function rather than for the degradation of specific substrates. Cleaves PINK1 in the mitochondrion.

**Summary**, from NCBI Gene [8192](https://www.ncbi.nlm.nih.gov/gene/8192):

> The protein encoded by this gene belongs to the peptidase family S14 and hydrolyzes proteins into small peptides in the presence of ATP and magnesium. The protein is transported into mitochondrial matrix and is associated with the inner mitochondrial membrane. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2084) · Entrez [8192](https://www.ncbi.nlm.nih.gov/gene/8192) · UniProt [Q16740](https://www.uniprot.org/uniprotkb/Q16740) · Ensembl [ENSG00000125656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125656)

## Data

Gene col 4640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4640); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4640]; `tensor/DDL_lfc|DDL_z.npy` [4640]; `embed/gene_vectors.npy` [4640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4640 or target_col == 4640). Every well: [[CLPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
