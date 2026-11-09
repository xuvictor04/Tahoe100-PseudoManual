---
symbol: "PIEZO2"
type: "gene"
col: 7848
ensembl_id: "ENSG00000154864"
name: "piezo type mechanosensitive ion channel component 2"
location: "18p11.22-p11.21"
module: 9
arm: "+"
pooled_cpm: 18.16
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PIEZO2

*piezo type mechanosensitive ion channel component 2* — 18p11.22-p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.40× (z +19.2, q 0e+00, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.744× (z -4.6, q 0.002, down in 9 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMCN1]] (+0.73, fdr 7e-06), [[LINC01116]] (+0.71, fdr 7e-06), [[DMD]] (+0.71, fdr 7e-06); moves opposite to [[ZDHHC9]] (-0.49, fdr 5e-05), [[MPG]] (-0.48, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CNTNAP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.40×** | +19.2 | 0e+00 | 12/17 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.54×** | +16.8 | 0e+00 | 10/15 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.54×** | +16.1 | 0e+00 | 9/11 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +15.4 | 0e+00 | 6/17 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +10.9 | 2e-25 | 9/15 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +9.8 | 8e-21 | 9/16 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +8.5 | 2e-15 | 11/18 (BT-474, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +6.9 | 4e-10 | 9/17 (SW 900, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +5.7 | 1e-06 | 7/17 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +5.5 | 3e-06 | 3/18 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 4/18 (A-172, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.5 | 3e-04 | 2/17 (A-172, A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 3/17 (HOP62, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.004 | 8/17 (SNU-423, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.028 | 12/18 (SK-MEL-2, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.744×** | -4.6 | 0.002 | 9/18 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.722×** | -3.6 | 0.063 | 5/17 (A-172, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -3.6 | 0.063 | 6/17 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.752× | -3.0 | 0.34 | 2/17 (BT-474, A-427) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0556× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.4) |
| [[BT-474 (line)]] | alt | 8.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 88.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +18.8) | [[Digitoxin (drug)]] 5 µM 0.148× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 189 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +19.5) | — |
| [[J82 (line)]] | alt | 8.64 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +8.9) | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 95.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.194× (z -8.6) |
| [[SW 900 (line)]] | alt | 7.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.7× (z +19.3) | — |
| [[C32 (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +9.6) | — |
| [[H4 (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 94.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.4) | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMCN1]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[LINC01116]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[DMD]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 | same gene group |
| [[FMN2]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[EGFEM1P]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SYNM]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[GRIK2]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[EPHA7]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[UNC5C]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LINC01687]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.60 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[NKAIN3]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | -0.49 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[MPG]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIEZO2's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3]] | B | PIEZO2 activity raises CNTNAP3's level | lines that do not express PIEZO2 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without PIEZO2 | 0.090 | ⚠ within organs, on part of the lines; also absent: AMPH, COLEC12, ANKRD30B |
| [[MYLK]] | C | PIEZO2 activity raises MYLK's level | lines that do not express PIEZO2 (30) vs lines expressing it (20) | 4.61× lower at baseline in the lines without PIEZO2 | 0.033 | ⚠ within organs, on part of the lines; also absent: AMPH, COLEC12, ANKRD30B; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, 29.7); signed map (39.5, 31.3). **Vector** length 58.7, 19.3% of its response variance represented; |z| ≥ 3 in 411 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +19.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | piezo type mechanosensitive ion channel component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22-p11.21 — chr18:10,666,483-11,149,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23403, FLJ23144, HsT748, HsT771, FLJ34907; previously FAM38B2, C18orf30, C18orf58, FAM38B |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes; Piezo type mechanosensitive ion channel components |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5I5](https://www.uniprot.org/uniprotkb/Q9H5I5) (Piezo-type mechanosensitive ion channel component 2):

> Pore-forming subunit of the mechanosensitive non-specific cation Piezo channel required for rapidly adapting mechanically activated (MA) currents and has a key role in sensing touch and tactile pain. Piezo channels are homotrimeric three-blade propeller-shaped structures that utilize a cap-motion and plug-and-latch mechanism to gate their ion-conducting pathways. Expressed in sensory neurons, is essential for diverse physiological processes, including respiratory control, systemic metabolism, …

**Summary**, from NCBI Gene [63895](https://www.ncbi.nlm.nih.gov/gene/63895):

> The protein encoded by this gene contains more than thirty transmembrane domains and likely functions as part of mechanically-activated (MA) cation channels. These channels serve to connect mechanical forces to biological signals. The encoded protein quickly adapts MA currents in somatosensory neurons. Defects in this gene are a cause of type 5 distal arthrogryposis. Several alternatively spliced transcript variants of this gene have been described, but their full-length nature is not known. …

**Accessions** — [HGNC:26270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26270) · Entrez [63895](https://www.ncbi.nlm.nih.gov/gene/63895) · UniProt [Q9H5I5](https://www.uniprot.org/uniprotkb/Q9H5I5) · Ensembl [ENSG00000154864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154864)

## Data

Gene col 7848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7848); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7848]; `tensor/DDL_lfc|DDL_z.npy` [7848]; `embed/gene_vectors.npy` [7848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7848 or target_col == 7848). Every well: [[PIEZO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIEZO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
