---
symbol: "NPR2"
type: "gene"
col: 8285
ensembl_id: "ENSG00000159899"
name: "natriuretic peptide receptor 2"
location: "9p13.3"
module: 181
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# NPR2

*natriuretic peptide receptor 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +3.8, q 0.057, up in 11 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.292× (z -12.4, q 3e-32, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRASP1]] (+0.68, fdr 1e-05), [[GLIPR1-AS1]] (+0.66, fdr 1e-05), [[BAAT]] (+0.65, fdr 3e-05); moves opposite to [[TMEM256]] (-0.58, fdr 1e-04), [[TMEM160]] (-0.56, fdr 1e-04), [[SBF2]] (-0.55, fdr 2e-04).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC25A11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.057 | 11/33 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.7 | 0.057 | 2/9 (SW480, PANC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.27× | +3.4 | 0.11 | 10/41 (A498, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 1.40× | +3.4 | 0.11 | 6/43 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.16 | 2/39 (SW1417, SW480) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.18 | 2/30 (SW 900, A549) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.37× | +3.0 | 0.19 | 3/32 (KATO III, HCT15, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.292×** | -12.4 | 3e-32 | 27/41 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.334×** | -11.0 | 8e-26 | 31/42 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.364×** | -10.2 | 6e-22 | 27/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.428×** | -8.5 | 2e-15 | 27/34 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.481×** | -7.4 | 2e-11 | 25/42 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.562×** | -5.8 | 6e-07 | 18/32 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.592×** | -5.3 | 1e-05 | 18/42 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.461×** | -4.1 | 0.003 | 12/38 (HCT15, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.696×** | -3.7 | 0.016 | 13/41 (hTERT-HPNE, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.67 | 0 | 4 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0843× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0969× (z -9.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LOX-IMVI (line)]] | wt | 6.82 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0665× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 9.58 | 0 | 2 | — | [[Penfluridol (drug)]] 5 µM 0.0612× (z -11.0) |
| [[SW480 (line)]] | alt | 7.14 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.184× (z -8.9) |
| [[A-427 (line)]] | wt | 3.05 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0485× (z -9.7) |
| [[A549 (line)]] | wt | 6.91 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0388× (z -13.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 5.32 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0622× (z -9.0) |
| [[C32 (line)]] | wt | 7.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -12.4) |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0907× (z -11.1) |
| [[LS 180 (line)]] | wt | 5.43 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0992× (z -9.2) ⚠ toxic; unreliable plate only |
| [[SW1417 (line)]] | alt | 3.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0728× (z -8.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRASP1]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[BAAT]] | +0.65 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SMIM15-AS1]] | +0.65 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[KLRA1P]] | +0.64 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CCDC17]] | +0.63 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[LRRC66]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MSH4]] | +0.62 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[AGER]] | +0.61 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TMED6]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[NLGN3]] | +0.61 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[C3orf20]] | +0.61 | +0.56 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM256]] | -0.58 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[TMEM160]] | -0.56 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[SBF2]] | -0.55 | -0.42 / -0.31 | both halves | 2e-04 | same gene group |
| [[PAFAH1B3]] | -0.55 | -0.41 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[NHP2]] | -0.54 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[ANTKMT]] | -0.54 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[SLC25A11]] | -0.54 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[METRN]] | -0.53 | -0.42 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NPR2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A11]] | B | NPR2 activity raises SLC25A11's level | lines that do not express NPR2 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without NPR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: POGLUT2, NPL |
| [[LINC03016]] | B | NPR2 activity raises LINC03016's level | lines that do not express NPR2 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without NPR2 | 0.094 | ⚠ within organs, on part of the lines; also absent: POGLUT2, NPL |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, -12.7); signed map (17.7, 3.1). **Vector** length 57.4, 7.88% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | natriuretic peptide receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,791,003-35,809,732 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GUCY2B, ANPb, GC-B; previously ANPRB, NPRB, AMDM |
| Gene groups (HGNC) | Transmembrane guanylate cyclases; DENN domain containing |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Physiological factors; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P20594](https://www.uniprot.org/uniprotkb/P20594) (Atrial natriuretic peptide receptor 2):

> Receptor for the C-type natriuretic peptide NPPC/CNP hormone. Has guanylate cyclase activity upon binding of its ligand. May play a role in the regulation of skeletal growth.

**Summary**, from NCBI Gene [4882](https://www.ncbi.nlm.nih.gov/gene/4882):

> This gene encodes natriuretic peptide receptor B, one of two integral membrane receptors for natriuretic peptides. Both NPR1 and NPR2 contain five functional domains: an extracellular ligand-binding domain, a single membrane-spanning region, and intracellularly a protein kinase homology domain, a helical hinge region involved in oligomerization, and a carboxyl-terminal guanylyl cyclase catalytic domain. The protein is the primary receptor for C-type natriuretic peptide (CNP), which upon ligand …

**Accessions** — [HGNC:7944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7944) · Entrez [4882](https://www.ncbi.nlm.nih.gov/gene/4882) · UniProt [P20594](https://www.uniprot.org/uniprotkb/P20594) · Ensembl [ENSG00000159899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159899)

## Data

Gene col 8285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8285); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8285]; `tensor/DDL_lfc|DDL_z.npy` [8285]; `embed/gene_vectors.npy` [8285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8285 or target_col == 8285). Every well: [[NPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
